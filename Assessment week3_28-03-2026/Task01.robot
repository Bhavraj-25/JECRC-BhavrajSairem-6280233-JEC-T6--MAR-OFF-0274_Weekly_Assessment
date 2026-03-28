*** Settings ***
Documentation    Myntra Handling
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.myntra.com/

*** Test Cases ***
Myntra Auto
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Mouse Over    xpath=(//a[text()='Women'])[1]
    Click Element    xpath=(//a[text()='Lehenga Cholis'])[1]

    Sleep  2s

    Scroll Element Into View    //input[@value='Blue']/following-sibling::div
    Click Element    //input[@value='Blue']/following-sibling::div

    Sleep  2s

    ${name}=  Get Text  //li[@id='32178529']/descendant::h3      # to get text
    Log To Console  ${name}

    Sleep  2s
    Close Browser