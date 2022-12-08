/* What should the add-on do after it is installed */
function onInstall() {
  onOpen();
}


/* What should the add-on do when a document is opened */
function onOpen() {
  DocumentApp.getUi()
  .createAddonMenu() // Add a new option in the Google Docs Add-ons Menu
  .addItem("Watch Me Work", "showSidebar")
  .addToUi();  // Run the showSidebar function when someone clicks the menu
}

/* Show a 300px sidebar with the HTML from googlemaps.html */
function showSidebar() {
  var html = HtmlService.createTemplateFromFile("watchmework")
    .evaluate()
    .setTitle("Watch Me Work"); // The title shows in the sidebar
  DocumentApp.getUi().showSidebar(html);
}

function getResults() {
  var doc = DocumentApp.getActiveDocument();
  var body = doc.getBody();

  var response = UrlFetchApp.fetch("https://watchmeworkapi.azure-api.net/WatchMeWorkAPI/HttpTrigger1");
  console.log(response);
}

function callAPI(text,fullText) {
  // Make a POST request
  let jsonBody = {
      "paragraph": text,
      "doc": fullText,
    }
  Logger.log(JSON.stringify(jsonBody))
  var options = {
    'method' : 'post',
    'payload' : JSON.stringify(jsonBody),
  };
 
  try {
    let output = UrlFetchApp.fetch('https://watchmeworkdeploy.azurewebsites.net/api/HttpTrigger1?code=9kfrKUk3iUOTeyvFIQtZEf3EIrmZdYQw9ybd7ttwcGbWAzFu6TCsXw==', options);
    let outputJson = JSON.parse(output.getContentText());
    Logger.log(outputJson.results.length == 0.0 || outputJson.entities.length == 0.0)
    if (outputJson.results.length != 0.0 || outputJson.entities.length != 0.0){
      return output;
    }
    else {
      return "No search results found";
    }
  } catch (err) {
    Logger.log(err)
    return "No search results found";
  }
}

function getParagraph() {
  try {
    const doc = DocumentApp.getActiveDocument();
    let cursorPosition = doc.getCursor();
    let text = cursorPosition.getSurroundingText().getText();
    if (!text){
      return "";
    }
    return text;
  } catch {
    return "";
  }
}

function getDoc() {
  try {
    return DocumentApp.getActiveDocument().getBody().getText();
  } catch {
    return "";
  }
}


function main(text) {
  let fullText = getDoc();
  if (text != "" && fullText != ""){
    let json = callAPI(text, fullText);
    if (json == "No search results found") {
      return json
    }
    return json.getContentText();
  }
  return "Empty string"
}

function clickTab(event,tabTitle) {
  tabContent = document.getElementsByClassName("tabContent")
  for (let i = 0; i < tabContent.length; i++) {
    tabContent[i].style.display = "none";
  }
  target = document.getElementById(tabTitle);
  target.style.display = "block";
}

