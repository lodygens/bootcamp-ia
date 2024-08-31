/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/ng2w1Mkd3dA
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/

/** Add fonts into your Next.js project:

import { Libre_Franklin } from 'next/font/google'
import { Arimo } from 'next/font/google'

libre_franklin({
  subsets: ['latin'],
  display: 'swap',
})

arimo({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
import { Button } from "@/components/ui/button"

export function Component() {
  return (
    <div className="container mx-auto px-4 py-8 sm:px-6 lg:px-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-primary-foreground">Most Popular Dishes</h1>
        <p className="text-muted-foreground">Check out the top-selling dishes at our restaurant.</p>
        <Button className="mt-4">Generate a new recipe</Button>
      </div>
      <div className="bg-background rounded-lg shadow-lg overflow-hidden">
        <table className="w-full table-auto">
          <thead>
            <tr className="bg-muted text-muted-foreground font-medium">
              <th className="px-6 py-4 text-left font-bold">Dish</th>
              <th className="px-6 py-4 text-right">Orders</th>
              <th className="px-6 py-4 text-right">Recipe</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-muted/20 bg-[#fdf7e8]">
              <td className="px-6 py-4 font-bold">Grilled Salmon with Lemon Butter</td>
              <td className="px-6 py-4 text-right font-medium">1,234</td>
              <td className="px-6 py-4 text-right">
                <Button>Generate Recipe</Button>
              </td>
            </tr>
            <tr className="border-b border-muted/20">
              <td className="px-6 py-4 font-bold">Beef Bolognese Pasta</td>
              <td className="px-6 py-4 text-right font-medium">987</td>
              <td className="px-6 py-4 text-right">
                <Button>Generate Recipe</Button>
              </td>
            </tr>
            <tr className="border-b border-muted/20">
              <td className="px-6 py-4 font-bold">Chicken Tikka Masala</td>
              <td className="px-6 py-4 text-right font-medium">876</td>
              <td className="px-6 py-4 text-right">
                <Button>Generate Recipe</Button>
              </td>
            </tr>
            <tr className="border-b border-muted/20">
              <td className="px-6 py-4 font-bold">Vegetable Stir-Fry</td>
              <td className="px-6 py-4 text-right font-medium">765</td>
              <td className="px-6 py-4 text-right">
                <Button>Generate Recipe</Button>
              </td>
            </tr>
            <tr>
              <td className="px-6 py-4 font-bold">Margherita Pizza</td>
              <td className="px-6 py-4 text-right font-medium">654</td>
              <td className="px-6 py-4 text-right">
                <Button>Generate Recipe</Button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}
