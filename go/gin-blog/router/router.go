package router

import (
	"gin-blog/controller"
	"github.com/gin-gonic/gin"
)

func Start() {
	r := gin.Default()
	r.LoadHTMLGlob("/gin-blog/templates/*")
	r.Static("/gin-blog/assets", "/assets")
	v1 := v1(r)
	{
		v1.GET(
			"login",
			controller.AddUser,
		)
	}
	r.Run()

}

func v1(r *gin.Engine) *gin.RouterGroup {
	return r.Group("/v1")
}
