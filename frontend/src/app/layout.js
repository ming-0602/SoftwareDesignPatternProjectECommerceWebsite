import localFont from "next/font/local";
import "./globals.css";
import {ThemeProvider} from "@/components/theme-provider";
import Head from "next/head";
import Link from "next/link";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata = {
  title: "Cloting",
  description: "Best Clothing",
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
        <Head>
            <link rel="shortcut icon" href="/favicon.ico"/>
        </Head>
        <body
            className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
        <ThemeProvider attribute={"class"} defaultTheme={"dark"} enableSystem disableTransitionOnChange>
            {children}
        </ThemeProvider>
        </body>
        </html>
    );
}
