import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { MinusIcon, PlusIcon, TrashIcon } from "lucide-react";
import { Input } from "@/components/ui/input";

const Cartitem = ({imageurl, Productname, Productquantity, Productprice}) => {
        return (
        <div className="flex justify-center">
            <Card className="m-4 w-2/3 shadow-lg rounded-lg border-gray-200">
                <CardContent className="flex items-center gap-6 p-6">
                    <img
                        src={imageurl}
                        alt="Product Image"
                        width={120}
                        height={120}
                        className="aspect-square overflow-hidden rounded-lg object-cover"
                    />
                    <div className="grid gap-2 w-full">
                        <div className="flex items-end justify-between">
                            <h3 className="font-bold text-2xl md:text-3xl">{Productname}</h3>
                            <div className="flex items-center gap-3 text-base">
                                <Button size="sm" variant="outline" className="p-1 hover:bg-gray-100">
                                    <MinusIcon className="w-4 h-4" />
                                    <span className="sr-only">Decrease</span>
                                </Button>
                                <Input readOnly type="number" defaultValue={Productquantity} className="w-14 text-center border-gray-300 rounded-md" />
                                <Button size="sm" variant="outline" className="p-1 hover:bg-gray-100">
                                    <PlusIcon className="w-4 h-4" />
                                    <span className="sr-only">Increase</span>
                                </Button>
                                <Button size="sm" variant="destructive" className="p-1 hover:bg-red-100">
                                    <TrashIcon className="w-4 h-4 text-red-600" />
                                    <span className="sr-only">Remove</span>
                                </Button>
                            </div>
                        </div>
                        <div className="text-gray-700 font-semibold text-lg">${Productprice}</div>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}

export default Cartitem;