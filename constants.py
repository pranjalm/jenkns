driverPath = '/usr/lib/chromium-browser/chromedriver'
gLink = "https://accounts.google.com"
identifierElement = "identifier"
## Give gmail id 
gmailId = "xyz@doctormm.com"

xpathNext = '//*[@id="identifierNext"]/span/span'
passElement = "password"
## Give gmailId password
gmailPass = "1234567890"

xpathLogin = '//*[@id="passwordNext"]/span/span'
ssUrl = "https://docs.google.com/spreadsheets/d/17pUrPnz7D-6pjqZkpG6VmlBhj2RBC3KsSP65dXON9hk/edit#gid=0"
ssApi = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
json = 'survey_cred.json'

## this variable is used for the google spreadsheet
ssName = 'NewSurvey_template_based1'  ## Spreadsheet name
sName = 'Template1'  ## sheet name

## change this variables to insert in sheet
data2Insert = ["pain1", "progress", "Since your pain began HOW HAS IT CHANGED?", "", "radio", "yes", "improved, worsened, stayed the same"]
insertIndex = 4

## Change this variable to delete the row 
deleteRow = 4

## change this variable to update the cell
updateRowNumber = 1
updateColNumber = 1
updateValue = "section"

xpathSsTools = '//*[@id="docs-tools-menu"]'
xpathSsToolsScriptEditor = '//*[@id=":gq"]/div/span'
xpathGsPublish = '//*[@id="macros-publish-menu"]'
xpathGsDeploy = '//*[@id=":1m"]'
xpathGsWebNew = '//*[@value="New"]'
xpathGsUpdate = '//*[@class="gwt-Button action submit"]' 
xpathGsLatestC = '//*[@id="dev-mode"]'
