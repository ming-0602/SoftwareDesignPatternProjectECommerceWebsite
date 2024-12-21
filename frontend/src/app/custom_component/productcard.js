// components/ProductCard.js

import React from 'react';
import Image from 'next/image';
// import { Card, CardBody, CardFooter, Button } from 'shadcn';
import {Card, CardContent, CardFooter, CardHeader, CardTitle} from "@/components/ui/card";
import {Button} from "@/components/ui/button";


const ProductCard = ({ imageSrc, productName, price, onAddToCart }) => {
    return (
        <Card className="w-full max-w-xs m-4">
            <div className="w-full h-48 relative">
                <Image
                    src={imageSrc}
                    alt={productName}
                    layout="fill"
                    objectFit="fill" // Stretch/compress image to fit container fully
                    className="w-full h-full"
                />
            </div>
            <CardHeader className="p-0.5 text-center">
                <CardTitle className="text-2xl truncate" title={productName}>{productName}</CardTitle>
            </CardHeader>
            <CardContent className="p-0.5 text-center">
                <p className="text-2xl font-semibold">${price}</p>
            </CardContent>
            <CardFooter className="mt-auto flex justify-center pb-2.5">
                <Button onClick={onAddToCart} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                        Add to Cart
                </Button>
            </CardFooter>
        </Card>
    );
};

export default ProductCard;
