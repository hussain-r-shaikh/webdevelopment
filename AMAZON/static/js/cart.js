// CSRF Cookie
function getCookie(name) {
    const cookies =
        document.cookie.split(";");
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (
            cookie.startsWith(
                name + "="
            )
        ) {
            return decodeURIComponent(
                cookie.substring(
                    name.length + 1
                )
            );
        }
    }
    return null;
}


class Cart {
    constructor() {
        this.items = JSON.parse(
            localStorage.getItem("cart")
        ) || [];
    }
    save() {
        localStorage.setItem(
            "cart",
            JSON.stringify(this.items)
        );
        this.updateCount();
    }
    add(product) {
        const item = this.items.find(
            item => item.product_id === product.product_id
        );
        if (item) {
            item.quantity += 1;
        } else {
            product.quantity = 1;
            this.items.push(product);
        }
        this.save();
    }
    remove(productId) {
        this.items = this.items.filter(
            item => item.product_id !== productId
        );
        this.save();
    }
    update(productId, quantity) {
        const item = this.items.find(
            item => item.product_id === productId
        );
        if (!item) {
            return;
        }
        if (quantity <= 0) {
            this.remove(productId);
        } else {
            item.quantity = quantity;
            this.save();
        }
    }
    total() {
        return this.items.reduce(
            (total, item) =>
                total + (
                    parseFloat(item.price) *
                    item.quantity
                ),
            0
        );
    }
    clear() {
        this.items = [];
        localStorage.removeItem("cart");
        this.updateCount();
    }
    updateCount() {
        const count = this.items.reduce(
            (total, item) =>
                total + item.quantity,
            0
        );
        $("#cart-count").text(count);
    }
    checkout() {
        if (this.items.length === 0) {
            alert("Your cart is empty.");
            return;
        }
        const data = this.items.map(
            item => ({
                product_id: item.product_id,
                quantity: item.quantity
            })
        );
        console.log("🚀Cart AJAX triggered...")
        console.log("Data: ", data);
        $.ajax({
            url: "/orders/cart/",
            type: "POST",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            data: JSON.stringify({
                items: data
            }),
            success: (response) => {
                this.clear();
                window.location.href =
                    response.redirect_url;
            },
            error: (response) => {
                const data =
                    response.responseJSON;
                if (
                    response.status === 401 &&
                    data.login_url
                ) {
                    window.location.href =
                        data.login_url;
                    return;
                }
                alert(
                    data?.message ||
                    "Unable to place order."
                );
            }
        });
    }
}
const cart = new Cart();
$(document).ready(function () {
    cart.updateCount();
});
