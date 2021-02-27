# TEST PLAN:

## Table no: High level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  H_01       |To check if the statistical analysis has produced all the required outputs such as max, medium, histogram, etc. |  Input modules with all values within boundaries|Statistical analysis for all inputs|Produced statistical analytical results for all inputs successfully|Requirement based |
|  H_02       |To check if the statistical analysis has produced all the required outputs such as max, medium, histogram, etc. |  Input modules with all values within boundaries|Statistical analysis for all inputs|Produced statistical analytical results only for students in one input module|Requirement based |
|  H_03       |To check if e-mail is triggered to every stakeholder. |  Module with e-mail IDs of stakeholders other than students |E-mail triggered to every stakeholder|Mails not triggered to stakeholders other than students |Scenario based    |
|  H_04       |To check if e-mail is triggered to every stakeholder. |  Module with e-mail IDs of stakeholders other than students |E-mail triggered to every stakeholder|Mails triggered to every stakeholders successfully |Scenario based    |
|  H_05       |To check if the results are not more than input rows |  Mark values of all students |Output rows same as input rows |Repetition of student IDs after input module integration|Boundary based    |
|  H_06       |To check if the results are not more than input rows |  Mark values of all students |Output rows same as input rows |All student IDs are integrated with their respective scores successfully |Boundary based    |

## Table no: Low level test plan

| **Test ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  L_01       |To check if empty values return a prompt |  Leave values empty in input modules|Prompt displayed mentioning missing value|Considering missing value as 0|Requirement based |
|  L_02       |To check if empty values return a prompt |  Leave values empty in input modules|Prompt displayed mentioning missing value|Prompt displayed with appropriate error/warning message|Requirement based |
|  L_03       |To check if multiple IDs with same mark are displayed in the right order depending on the alphabetical order |  Scores resulting to same total values for multiple IDs|IDs displayed in alphabetically ascending order for same total values|IDs displayed with corresponding marks in alphabetical order successfully|Scenario based    |
|  L_04       |To check if multiple IDs with same mark are displayed in the right order depending on the alphabetical order |  Scores resulting to same total values for multiple IDs|IDs displayed in alphabetically ascending order for same total values|IDs displayed with corresponding marks are not in alphabetical order |Scenario based    |
|  L_05       |To prompt if the e-mail IDs are in incorrect format |  Enter email IDs incorrectly |Prompt displaying asking to correct the incorrect e-mail ID|Accepts incorrect e-mail ID and fails to send the mail |Boundary based    |
|  L_06       |To prompt if the e-mail IDs are in incorrect format |  Enter email IDs incorrectly |Prompt displaying asking to correct the incorrect e-mail ID|Prompt displayed with appropriate error/ warning message |Boundary based    |
