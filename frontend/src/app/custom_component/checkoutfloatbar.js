import {Button} from "@/components/ui/button";

const Checkoutbar = ({originalTotal, discountedTotal }) => {
  return(
      <div
          className="fixed bottom-0 left-0 right-0 bg-black shadow-md p-4 flex justify-between items-center border-t border-gray-300">
          <div className="flex flex-col">
              <span className="text-sm text-gray-500">Original Total:</span>
              <span className="font-bold text-lg">${originalTotal}</span>
          </div>
          <div className="flex flex-col">
              <span className="text-sm text-gray-500">Discounted Total:</span>
              <span className="font-bold text-lg">${discountedTotal}</span>
          </div>
          <Button variant="ghost" className="ml-4">
              Checkout
          </Button>
      </div>
  )
}

export default Checkoutbar;