package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:     "root",
	Short:   "Short",
	Long:    "Long",
	Example: "Example",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("start..............")
		fmt.Println("end................")
	},
}

func Execute() {
	rootCmd.Execute()

}
