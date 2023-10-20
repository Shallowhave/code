package main

import (
	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
	"log"
	"strconv"
)

func SendMessage(update tgbotapi.Update, bot *tgbotapi.BotAPI) {

	userID := update.Message.From.ID
	//
	//// 获取消息中的群组ID
	//groupID := update.Message.Chat.ID
	//
	//// 获取消息中的频道ID
	//channelID := update.Message.Chat.ID
	msg := tgbotapi.NewMessage(update.Message.Chat.ID, update.Message.Text+"\n"+strconv.FormatInt(userID, 10))
	msg.ReplyToMessageID = update.Message.MessageID
	bot.Send(msg)
}



func main() {
	bot, err := tgbotapi.NewBotAPI("5560879143:AAF90mZvZ2UofCwk7li1ZWLrufJXv4mVd2Y")
	if err != nil {
		log.Panic(err.Error())
	}

	bot.Debug = true

	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message != nil { // If we got a message
			log.Printf("[%s] %s", update.Message.From.UserName, update.Message.Text)

			if update.Message.Chat.Type == "private" {
				//userID := update.Message.From.ID
				//
				go SendMessage(update, bot)
				//是用户消息
			}
			if update.Message.Chat.Type == "group" {
				// 是群组消息
			}
			if update.Message.Chat.Type == "channel" {
				// 是频道消息
			}

		}

	}
}
