// src/components/ImageUploader.js
import React, { useState } from 'react';    //useState means remembering something
import axios from 'axios';
import styles from './ImageUploader.module.css'

function ImageUploader() {
    const [image, setImage] = useState(null);   //I guess this line distribute an image space
    const [imageFile, setImageFile] = useState(null);   //They are var and function to update it.
    const [processedImage, setProcessedImage] = useState(null);

    const handleImageChange = (e) => {
        if (e.target.files && e.target.files[0]) {
            let imgFile = e.target.files[0];
            setImageFile(imgFile);
            setImage(URL.createObjectURL(imgFile));
        }
    };

    const handleProcessImage = async () => {
        const formData = new FormData();
        formData.append('image', imageFile);

        try {
            const response = await axios.post('http://localhost:8000/image_processor/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setProcessedImage(`data:image/jpeg;base64,${response.data.image}`);
        } catch (error) {
            console.error("Error during image processing", error);
        }
    };

    return (
        <div className={styles.container}>
            <div className={styles.imageSection}>
                <input type="file" onChange={handleImageChange}/>
                {image && <div>
                    <h2>上传的图片：</h2>
                    <img src={image} alt="Uploaded" className={styles.image}/>
                </div>}
            </div>
            <div className={styles.imageSection}>
                <button onClick={handleProcessImage}>处理图片</button>
                {processedImage && <div>
                    <h2>处理后的图片：</h2>
                    <img src={processedImage} alt="Processed" className={styles.image}/>
                </div>}
            </div>
        </div>
    );
}

export default ImageUploader;