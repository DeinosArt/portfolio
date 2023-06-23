"use client"

import { SuperImage } from "../components/images"
import {useState, useEffect} from "react"

const portfolioPage = () => {
  const [data, setData] = useState();

  const changeImage = async () => {
    const randomImage = await (
      await fetch(
        "http://localhost:5000/image"
      )
    ).json();
    console.log(randomImage)

    // set state when the data received
    setData(randomImage);
  };

  useEffect(() => {
    // fetch data
    changeImage()
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h2>here is an image !</h2>
      <SuperImage
        url={data}
      />
      <button onClick={changeImage}>
        change l'image
      </button>
    </main>
  )
}

export default portfolioPage