import React from "react";
import "./navigation.scss";

export default function Navigation() {
    return (
        <nav className="Navigation">
            <div className="nav-logo container">
                <img src="/logo.svg" alt="Logo" />
                <span className="text-primary">fashion gallery</span>
            </div>
        </nav>
    )
}