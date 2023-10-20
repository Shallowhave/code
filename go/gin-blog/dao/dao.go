package dao

import (
	"gin-blog/model"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type manager struct {
	Db  *gorm.DB
	Err error
}

func (m manager) AddUser(user *model.User) {
	m.Db.Create(&user)

}

type Manager interface {
	AddUser(user *model.User)
}

var Mgr Manager

func init() {

	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}
	Mgr = &manager{
		Db:  db,
		Err: err,
	}

	db.AutoMigrate(&model.User{})

	// Create

}
