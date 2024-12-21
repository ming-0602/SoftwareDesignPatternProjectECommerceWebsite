"use client"

import Slideshow from "@/app/custom_component/slideshow";
import NavigationMenu from "@/app/custom_component/navbar";
import {useEffect, useState} from "react";
import ProductCard from "@/app/custom_component/productcard";

export default function Home() {
    const [products, setProducts] = useState([]);
    const [cartMessages, setCartMessages] = useState("");

    useEffect(() => {
        async function fetchProducts() {
            const response = await fetch('http://127.0.0.1:5001/api/products?limit=3');
            const data = await response.json();
            setProducts(data);
        }
        fetchProducts();
    }, []);


    const handleAddtoCart = async (productName, productid, productimg, productprice) => {
        try {
            const response = await fetch('http://127.0.0.1:5002/api/cart/', { // Replace with your Flask API URL for cart
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_name: productName,
                    // cart_id: productid,
                    product_price: parseFloat(productprice),
                    product_image: productimg,
                    product_quantity: parseFloat(1),
                }),
            });

            if (!response.ok) {
                throw new Error('Failed to add product to cart');
            }

            const result = await response.json();
            alert(`${productName} added to cart`);
            setCartMessages(result.message); // Assuming your API returns a message
        } catch (error) {
            console.error('Error adding to cart:', error);
            alert('Error adding to cart');
        }
    }

        return (
            <div>
                <NavigationMenu></NavigationMenu>
                <Slideshow></Slideshow>
                {/*<ProductcardMainPage></ProductcardMainPage>*/}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-0.5 p-4 content-center">
                    {products.map(product => (
                        <ProductCard
                            key={product.id}
                            imageSrc={product.image_url}
                            productName={product.name}
                            price={product.price}
                            onAddToCart={() => handleAddtoCart(product.name, product.id , product.image_url, product.price)}
                        />
                    ))}
                </div>


            </div>
    );
}
