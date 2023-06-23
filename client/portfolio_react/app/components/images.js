import Image from 'next/image'
 

const SuperImage = ({url}) => {
    console.log("SuperImage", url)
    let imageUrl = undefined
    if(url) {
        imageUrl = url[1]
    }else {
        imageUrl = undefined
    }
    return (
        <Image
        src={imageUrl}
        width={500}
        height={500}
        alt="Picture of the author"
        />
    );
};


export {SuperImage}
