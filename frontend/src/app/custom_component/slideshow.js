import React from 'react';
import { Card, CardHeader } from "@/components/ui/card";
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel";

export default function Slideshow() {
    const images = [
        { src: "https://media.gq.com/photos/66d23677ee22dbb7a373b293/16:9/w_2560%2Cc_limit/uniqlo-shopping-lede=2.png", alt: "Placeholder image 1" },
        { src: "https://www.japantimes.co.jp/uploads/imported_images/uploads/2023/01/np_file_207687.jpeg ", alt: "Placeholder image 2" },
    ];

    return (
        <Card className="w-full">
            <CardHeader>
                <Carousel className="w-full">
                    <CarouselContent>
                        {images.map((image, index) => (
                            <CarouselItem key={index}>
                                <div className="relative w-full h-[400px]">
                                    <img
                                        src={image.src}
                                        alt={image.alt}
                                        className="w-full h-full object-fill"
                                    />
                                </div>
                            </CarouselItem>
                        ))}
                    </CarouselContent>
                    <CarouselPrevious className="absolute left-4 top-1/2 transform -translate-y-1/2" />
                    <CarouselNext className="absolute right-4 top-1/2 transform -translate-y-1/2" />
                </Carousel>
            </CardHeader>
        </Card>
    );
}