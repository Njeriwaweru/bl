"use client";
import React, { useEffect, useState } from 'react';
import Image from 'next/image';

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/categories/debug')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setCategories(data);
      })
      .catch(error => {
        setError(error);
      });
  }, []);
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div className='mx-4 md:mx-22 lg:mx-52 grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4'>
        {categories.length > 0? categories.map((category,index) => (
            <div className='flex flex-col items-center justify-center gap-2 bg-purple-50 p-5 rounded-lg
             cursor-pointer hover:scale-110 transition-all ease-in-out'>
                <img src={category.icon} alt={category.name} width={35} height={35} />
                <h2 className='text-primary'>{category.name}</h2>
            </div>
        )):
            [1,2,3,4,5].map((item,index)=>(
                <div className='h-[120px] w-full bg-slate-200 animate-pulse rounded-lg'>
                </div>
            ))
        }
    </div>
  );
};

export default Categories;
