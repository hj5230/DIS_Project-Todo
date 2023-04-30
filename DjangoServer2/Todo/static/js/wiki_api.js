const titleElements = document.querySelectorAll(".title");

const createPopupPanel = async (titleText) => {
  const popupPanel = document.createElement("div");
  popupPanel.classList.add("panel");
  popupPanel.classList.add("panel-default");
  popupPanel.style.position = "fixed";
  popupPanel.style.top = "50%";
  popupPanel.style.left = "50%";
  popupPanel.style.transform = "translate(-50%, -50%)";
  popupPanel.style.backgroundColor = "white";
  popupPanel.style.padding = "20px";
  popupPanel.style.zIndex = "1000";
  const closeButton = document.createElement("button");
  closeButton.classList.add("btn")
  closeButton.classList.add("btn-primary")
  closeButton.innerHTML = `<span class="glyphicon glyphicon-remove"></span>`;
  closeButton.addEventListener("click", () => {
    popupPanel.remove();
  });
  const pro = await fetch(`http://127.0.0.1:6999/getwiki/${titleText}`);
  const wikiBody = await pro.json();
  const popupTitle = document.createElement("h2");
  popupTitle.textContent = titleText;
  const wikiBodyElement = document.createElement("p");
  wikiBodyElement.innerHTML = wikiBody;
  popupPanel.appendChild(popupTitle);
  popupPanel.appendChild(wikiBodyElement);
  popupPanel.appendChild(closeButton);
  return popupPanel;
};

titleElements.forEach((title) => {
  title.addEventListener("click", async () => {
    const titleText = title.textContent;
    const popupPanel = await createPopupPanel(titleText);
    document.body.appendChild(popupPanel);
  });
});
