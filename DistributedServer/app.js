const express = require("express");
const cookieParser = require("cookie-parser");
const logger = require("morgan");
const cors = require("cors");

const app = express();

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(cors());

app.get("/gettemp", async (req, res) => {
  import("node-fetch").then(({ default: fetch }) => {
    (async () => {
      const now = new Date();
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, "0");
      const day = String(now.getDate()).padStart(2, "0");
      const hour = String(now.getHours()).padStart(2, "0");
      const datetime = `${year}-${month}-${day}T${hour}:00`;
      const url =
        "https://api.open-meteo.com/v1/forecast?latitude=60.17&longitude=24.94&hourly=temperature_2m";
      const response = await fetch(url);
      const data = await response.json();
      const index = data.hourly.time.indexOf(datetime);
      const temp = data.hourly.temperature_2m[index];
      res.send({
        temp: temp,
      });
    })();
  });
});

app.get("/getwiki/:item", async (req, res) => {
  const { item } = req.params;
  import("node-fetch").then(({ default: fetch }) => {
    (async () => {
      const wikiPro = await fetch(
        `https://en.wikipedia.org/api/rest_v1/page/summary/${decodeURIComponent(
          item
        )}`
      );
      const wikiRes = await wikiPro.json();
      const extractHTML = wikiRes.extract_html;
      if (extractHTML) res.json(extractHTML);
      else res.json("<p>Nothing was found from wiki</p>");
    })();
  });
});

module.exports = app;
