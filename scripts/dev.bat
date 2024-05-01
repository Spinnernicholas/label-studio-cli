@echo off
:: +-----------------------------------+
:: | Project Development Tools CLI     |
:: +-----------------------------------+

:: Parse the command line arguments
call :parseArgs %*
:: Init CLI help information
call :helpDocs

:: +-----------------------------------+
:: | CLI Command Declarations          |
:: +-----------------------------------+

:: Command help
call :registerCommand "help" "Show this help message"
:command_help
if defined RUNNING (
    call :printDocs
    goto :EOF
)

:: +-----------------------------------+
:: | Docker Dev Server Commands        |
:: +-----------------------------------+

:: Command up
call :registerCommand "up" "Start the application"
:command_up
if defined RUNNING (
    :: Actually run the command
    call :getRunningContainerId
    if not defined container_id (
        echo docker-compose up -d%args%
        docker-compose up -d%args%
    ) else (
        echo The application is already running
    )
    goto :EOF
)

:: Command down
call :registerCommand "down" "Stop the application"
:command_down
if defined RUNNING (
    call :getRunningContainerId
    if defined container_id (
    echo docker-compose down%args%
    docker-compose down%args%
    ) else (
        echo The application is not running
    )
    goto :EOF
)

:: Command shell
call :registerCommand "shell" "Open a shell in the application container"
:command_shell
if defined RUNNING (
    call :getRunningContainerId
    if defined container_id (
        echo docker exec -it %container_id% /bin/bash
        docker exec -it %container_id% /bin/bash
    ) else (
        echo The application is not running
    )
    goto :EOF
)

:: Command exec
call :registerCommand "exec" "Execute a command in the application container"
:command_exec
if defined RUNNING (
    call :getRunningContainerId
    if defined container_id (
        echo docker exec %container_id%%args%
        docker exec %container_id%%args%
    ) else ( 
        echo The application is not running
    )
    goto :EOF
)

:: +-----------------------------------+
:: | Run Command or Show Help          |
:: +-----------------------------------+

call :runCommand

exit

echo "This should never be reached"

:: +-----------------------------------+
:: | CLI Tool Functions                |
:: +-----------------------------------+

:parseArgs

set "command=%~1"
if "%command%"=="" set "command=help"
set "args="
shift

:loop
if "%~1"=="" goto :end
set "args=%args% %1"
shift
goto loop
:end
set "function_call=command_%command%%args%"
goto :EOF

:: Init CLI help docs
:helpDocs
set "help_lines[1]=Project CLI DevTools"
set "help_lines[2]=Usage: dev [command] [args]"
set "help_lines[3]="
set "help_lines[4]=Commands:"
set "help_line_count=4"
goto :EOF

:: Add CLI help docs
:registerCommand
set "command[%~1]=true"
set /a help_line_count+=1
set "padded=%~1      "
set "padded=%padded:~0,6%
set "help_lines[%help_line_count%]=  %padded% - %~2"
goto :EOF

:: Print CLI help docs
:printDocs
for /l %%i in (1,1,%help_line_count%) do (
    call echo.%%help_lines[%%i]%%
)
goto :EOF

:: Run the command
:runCommand
set "RUNNING=true"
call set "command_check=%%command[%command%]%%"
if not defined command_check (
    echo Invalid command: %command%
    call :printDocs
    exit /b 1
) else (
    call :%function_call%
)
goto :EOF

:: +-----------------------------------+
:: | Additional Helper Functions       |
:: +-----------------------------------+

:: Check if Docker Compose is already running
:getRunningContainerId
for /f "tokens=*" %%a in ('docker-compose ps -q ls-cli-dev') do set container_id=%%a
goto :EOF