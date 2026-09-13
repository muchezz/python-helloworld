const express = require("express");
const app = express();
app.get("/", (req, res) => res.status(200).send("Phase 6B Express acceptance"));
app.listen(process.env.PORT, () => console.log("listening on", process.env.PORT));
