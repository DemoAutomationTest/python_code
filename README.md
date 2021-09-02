Hi 我是一名軟體測試工程師  
在不同行業經歷各種測試需求  
我認為手動測試與自動化測試    
對軟體開發過程中是輔助軟體品質的其中一環  
皆有其必要性  
當然最重要的  
還是團隊間每位成員  
都要對自己的產出盡一份力  

在這裡建立了網頁自動化、行動裝置自動化的範例  
歡迎一起交流   

-PC版網頁自動化
[點我](https://github.com/DemoAutomationTest/python_code/tree/master/selenium_case/test_case)  

主要運用的語言Python
其他應用
Test framework

**pytest、Allure** 

Web test 

**Selenium**  

Mobile test

**Airtest**  

下圖我以網頁版網路銀行轉帳為例  
解釋自動化測試規劃的架構  
### 【操作行為(函數化)】
  - 登入網路銀行    
  - 進入轉帳功能  
  - 輸入轉帳資訊(轉出帳號\轉入帳號\轉出金額...)   
  - 登出網路銀行    

### 【解說】  
test_case建立一個pytest架構的檔案  
在執行案例中呼叫  
-引用測試資料(如登入帳號從資料表取出)  
-登入/登出函數  
-轉帳操作函數(輸入參數有轉出帳戶、轉入帳號、金額)  
-輸出測試報告  
### 優點：  
- 以頁面為單位設計函數，對於大型且多人合作的專案，可以簡化長期維護成本   

### 缺點：  
- 初期規劃架構較為費時費工  
![image](https://github.com/DemoAutomationTest/python_code/blob/master/test_flow.JPG)
