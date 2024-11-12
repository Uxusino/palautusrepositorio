*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    pekka
    Set Password    pekka123
    Set Password Confirmation    pekka123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username    a
    Set Password    aaaa1111
    Set Password Confirmation    aaaa1111
    Submit Credentials
    Register Should Fail With Message    Username is too short

Register With Valid Username And Too Short Password
    Set Username    pekka
    Set Password    pek123
    Set Password Confirmation    pek123
    Submit Credentials
    Register Should Fail With Message    Password must be longer than 8 symbols

Register With Valid Username And Invalid Password
    Set Username    pekka
    Set Password    pekkasama
    Set Password Confirmation    pekkasama
    Submit Credentials
    Register Should Fail With Message    Password must contain at least one numerical or special symbol

Register With Nonmatching Password And Password Confirmation
    Set Username    pekka
    Set Password    pekka123
    Set Password Confirmation    pekka321
    Submit Credentials
    Register Should Fail With Message    Password and Password Confirmation don't match!

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    pekka123
    Set Password Confirmation    pekka123
    Submit Credentials
    Register Should Fail With Message    Username already in use

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}