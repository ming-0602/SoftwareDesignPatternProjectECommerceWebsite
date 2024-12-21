'use client';
import NavigationMenu from "@/app/custom_component/navbar";
import Cartitem from "@/app/custom_component/cartitem";
import { useEffect, useState } from "react";
import Checkoutbar from "@/app/custom_component/checkoutfloatbar";

export default function Page() {
    const [carts, setCarts] = useState([]);
    const [original_total, setOriginalTotal] = useState(0);
    const [discounted_total, setDiscountedTotal] = useState(0);

    useEffect(() => {
        const fetchCart = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5002/api/cart/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();

                console.log(data); // Check the structure of data

                // Set carts to the items array from the response
                setCarts(data.items || []);
                setOriginalTotal(data.original_total || 0);
                setDiscountedTotal(data.discounted_total || 0);

                // Log updated totals after setting state
                console.log("Original Total:", data.original_total);
                console.log("Discounted Total:", data.discounted_total);
            } catch (error) {
                console.error('Error fetching carts:', error);
            }
        };
        fetchCart();
    }, []);

    return (
        <div>
            <NavigationMenu />
            <div className="flex-grow overflow-y-auto p-4 pb-20">
                {carts.length > 0 ? (
                    carts.map((cart, index) => (
                        <Cartitem
                            key={index} // Use index or cart.id if available
                            imageurl={cart.product_image}
                            Productname={cart.product_name}
                            Productquantity={cart.product_quantity}
                            Productprice={cart.product_price}
                        />
                    ))
                ) : (
                    <p>No items in the cart.</p>
                )}
            </div>


            <Checkoutbar
                discountedTotal={discounted_total.toFixed(2)}
                originalTotal={original_total.toFixed(2)}
            />
        </div>
    );
}
