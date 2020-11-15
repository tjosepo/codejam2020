import { Button, Portal } from "@material-ui/core";
import React, { useState } from "react";
import { QueryImage } from "../interfaces";
import { CDN, INC } from "../queries";
import "./gallery.scss";
import "bootstrap/js/dist/modal"

interface Props {
    images: QueryImage[];
    search: string;
}

export default function Gallery({ images, search }: Props) {
    const [selectedImg, setSelectedImg] = useState<QueryImage>();

    const openModal = (image: QueryImage) => {
        setSelectedImg(image);
        fetch(INC(image.id, search));
    }

    return (
        <div className="Gallery">
            <div className="grid">
                {images.map((image) =>
                    <button key={image.id} type="button" data-toggle="modal" data-target="#imageModal" onClick={() => openModal(image)}>
                        <img src={CDN(image.file)} alt="product" />
                    </button>
                )}
            </div>

            <Portal>
                <div className="modal" id="imageModal" tabIndex={-1}>
                    <div className="modal-dialog modal-fullscreen">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Product</h5>
                                <button type="button" className="btn-close" data-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div className="modal-body">
                                {selectedImg && <img src={CDN(selectedImg.file)} alt="Selected" />}
                                <div>
                                    <p className="lead">Product name</p>
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                                    <div style={{ display: 'flex' }}>
                                        <input type="radio" name="size" value="XS" id="XS" hidden />
                                        <label htmlFor="XS" className="mr-2">XS</label>

                                        <input type="radio" name="size" value="S" id="S" hidden />
                                        <label htmlFor="S" className="mr-2">S</label>

                                        <input type="radio" name="size" value="M" id="M" hidden />
                                        <label htmlFor="M" className="mr-2">M</label>

                                        <input type="radio" name="size" value="L" id="L" hidden />
                                        <label htmlFor="L" className="mr-2">L</label>

                                        <input type="radio" name="size" value="XL" id="XL" hidden />
                                        <label htmlFor="XL" className="mr-2">XL</label>
                                    </div>
                                </div>
                            </div>
                            <div className="modal-footer">
                                <Button variant="contained" data-dismiss="modal" className="mr-2">Close</Button>
                                <Button variant="contained" color="primary">
                                    Add to Cart
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            </Portal>
        </div>
    )
}