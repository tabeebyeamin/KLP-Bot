# Kijiji Lowest Price Bot
## If you have any suggestions, please let me know!
Submit Issues or let me know however you can. I want to make this project something that people actually want to use so I appreciate all the feedback possible. Tell me what should I add to make it something you would want to use?

-------------------------------------------------------------------------------

Give it the product your looking for and your location and it will find the lowest price listing of that product on Kijiji. You can use it as a Slack Bot!
Uses Python and BS4 and SQLite3 for database entry.
This program works really well with products with easily identifiable model names or numbers, like computer hardware and peripherals, but it will also work on a plethora of other products as shown below. This is how it works right now. I'm always looking to add more features and functionality. If you have any issues or suggestions, please let me know.

-------------------------------------------------------------------------
## Use it as a Script
![alt_text](https://i.imgur.com/BufaLcg.png)

## Save Your Findings to a Database!
![alt_text](https://i.imgur.com/a5B5WTg.png)
![alt_text](https://i.imgur.com/jJ2Lb9T.png)

-------------------------------------------------------------------------
# Use it with Slack!
## Help
![alt_text](https://i.imgur.com/Yrm9J3l.png)

## Locations
![alt_text](https://i.imgur.com/Iy0pQhT.png)

## Peek
![alt_text](https://i.imgur.com/Ju1uKkr.png)
![alt_text](https://i.imgur.com/6yAFqCk.png)

## Peek and Save
![alt_text](https://i.imgur.com/L7SPHba.png)


## Todo
- change save to database command as:

1. **save** *productname* **in** *locationnum* **to** *databasename*
2. **save** *productname* **in** *locationnum* (not providing *to* will save to default.db)
- Fix issues with Quebec
- Minimum Price to filter false results
- Return multiple i.e "n cheapest items" to mitigate inaccuracy
- Error Handling
- Discord Bot Functionality
- GUI for Slack/Discord Bot
- Make a Logo
- Monitoring Using Proxies
- Messenger Bot?
- Make it able to send Kijiji user a message on their posting
- Turn into web application so users don't have to download
