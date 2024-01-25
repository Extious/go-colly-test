package main  
  
import (  
 "fmt"  
 "log"  
  
 selenium "github.com/lotabout/go-selenium"  
)  
  
func main() {  
 // 创建Selenium WebDriver实例  
 driver, err := selenium.NewChromeDriver()  
 if err != nil {  
 log.Fatal(err)  
 }  
 defer driver.Quit()  
  
 // 打开网页  
 err = driver.Get("https://www.example.com")  
 if err != nil {  
 log.Fatal(err)  
 }  
  
 // 查找元素并获取链接地址  
 element, err := driver.FindElement(selenium.ByCSSSelector{"a"})  
 if err != nil {  
 log.Fatal(err)  
 }  
 link, err := element.GetAttribute("href")  
 if err != nil {  
 log.Fatal(err)  
 }  
 fmt.Println(link)  
}