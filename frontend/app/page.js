import Image from "next/image";
import Hero from "./_components/Hero";
import Categories from "./_components/Categories";


export default function Home() {
  return (
    <div>
      <Hero />
      <Categories />
    </div>
  );
}
