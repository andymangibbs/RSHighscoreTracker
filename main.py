import apiPuller
import excelWrite
import excelRead
import excelUpdate

# consider adding support for main or reg irons
userInput = input("Create new excel sheet?(y/n): ")
keyword = "iron_andyman"#input("Enter character name, underscore for spaces: ")
highscores = apiPuller.api_pull(keyword)
if userInput == 'y':
    excelWrite.excel_writer(keyword, highscores)
elif userInput == 'n':
    last = excelRead.excel_reader(keyword)
    excelUpdate.excel_update(keyword, last, highscores)
