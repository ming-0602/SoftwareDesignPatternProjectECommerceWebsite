'use client'
import React from 'react';
import {Button} from "@/components/ui/button";
import Link from "next/link";

export default function NavigationMenu() {
    const toggleMenu = () => {
        const menu = document.getElementById("mobile-menu");
        menu.classList.toggle("hidden");
    };

    return (
        <nav className="bg-black border-b shadow-md">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex-shrink-0 flex items-center">
                        <h1 className="text-2xl font-bold">Clothing</h1>
                    </div>

                    {/* Desktop Menu */}
                    <div className="hidden sm:flex sm:items-center space-x-4">
                        <Link href={"/"}>
                            <Button variant={"ghost"} >Home</Button>
                        </Link>
                        <Link href={"/product"}>
                            <Button variant={"ghost"} >Product</Button>
                        </Link>
                        <Link href={'/cart'}>
                            <Button variant={"ghost"} >Cart</Button>
                        </Link>
                    </div>

                    {/* Mobile Menu Button */}
                    <div className="sm:hidden flex items-center">
                        {/*<button onClick={toggleMenu} className="text-gray-500 hover:text-blue-500">*/}
                        {/*    Menu*/}
                        {/*</button>*/}
                        <Button variant={"ghost"} onClick={toggleMenu}>
                            Menu
                        </Button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            <div id="mobile-menu" className="hidden sm:hidden">
                <div className="space-y-1 px-2 pt-2 pb-3">
                    <Link href={"/"}>
                        <Button variant={"ghost"} size={"lg"} className={"block w-full"}>Home</Button>
                    </Link>
                    <Link href={"/product"}>
                        <Button variant={"ghost"} size={"lg"} className={"block w-full"}>Product</Button>
                    </Link>
                    <Link href={"/cart"}>
                        <Button variant={"ghost"} size={"lg"} className={"block w-full"}>Cart</Button>
                    </Link>
                </div>
            </div>
        </nav>
    );
}
