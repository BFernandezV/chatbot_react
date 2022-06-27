import React from "react";
import "../css/ProfileBot.css";
import Bot from "../images/bot.png";

const ProfileBot = () => {
  return (
    <div className="d-flex gap-3 p-4 bodyProfile">
      <img
        src={Bot}
        alt="Profile Hachiko"
        className="img-fluid bodyNavBar__img"
      ></img>
      <div className="d-flex flex-column text-start h-50">
        <h4 className="text-white">Hachikō</h4>
        <h6 className="text-secondary">En linea</h6>
      </div>
    </div>
  );
};

export default ProfileBot;
