package controller

import (
	"gin-blog/dao"
	"gin-blog/model"
	"github.com/gin-gonic/gin"
)

func AddUser(context *gin.Context) {
	user := model.User{}
	context.Bind(&user)
	dao.Mgr.AddUser(&user)

}
