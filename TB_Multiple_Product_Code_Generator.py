# -*- coding: utf-8 -*-  
number_of_products = 1

## Params part
print "Params"
for i in range(0, number_of_products):
    print "    Numeric RiskRatio" + i.__str__() + "(1);                   // % Risk Per N ( 0 - 100)"
    print "    Numeric ATRLength" + i.__str__() + "(20);                  // 平均波动周期 ATR Length"
    print "    Numeric boLength" + i.__str__() + "(20);                   // 短周期 BreakOut Length"
    print "    Numeric fsLength" + i.__str__() + "(55);                   // 长周期 FailSafe Length"
    print "    Numeric teLength" + i.__str__() + "(10);                   // 离市周期 Trailing Exit Length"
    print "    Bool LastProfitableTradeFilter" + i.__str__() + "(True);   // 使用入市过滤条件"
    print ""
    
## Vars part
print "Vars"
print "    Numeric TotalEquity;                    // 按最新收盘价计算出的总资产"
for i in range(0, number_of_products):
    print "    Numeric MinPoint" + i.__str__() + ";                       // 最小变动单位"
    print "    NumericSeries AvgTR" + i.__str__() + ";					// ATR"
    print "    Numeric N" + i.__str__() + ";                              // N 值"
##    print "Numeric TotalEquity" + i.__str__() + ";                    // 按最新收盘价计算出的总资产"
    print "    Numeric TurtleUnits" + i.__str__() + ";                    // 交易单位"
    print "    NumericSeries DonchianHi" + i.__str__() + ";              	// 唐奇安通道上轨，延后1个Bar"
    print "    NumericSeries DonchianLo" + i.__str__() + ";              	// 唐奇安通道下轨，延后1个Bar"
    print "    NumericSeries fsDonchianHi" + i.__str__() + ";            	// 唐奇安通道上轨，延后1个Bar，长周期"
    print "    NumericSeries fsDonchianLo" + i.__str__() + ";            	// 唐奇安通道下轨，延后1个Bar，长周期"
    print "    Numeric ExitHighestPrice" + i.__str__() + ";               // 离市时判断需要的N周期最高价"
    print "    Numeric ExitLowestPrice" + i.__str__() + ";                // 离市时判断需要的N周期最低价"
    print "    Numeric myEntryPrice" + i.__str__() + ";                   // 开仓价格"
    print "    Numeric myExitPrice" + i.__str__() + ";                    // 平仓价格"
    print "    Bool SendOrderThisBar" + i.__str__() + "(False);          	// 当前Bar有过交易"
    print "    NumericSeries preEntryPrice" + i.__str__() + "(0);       	// 前一次开仓的价格"
    print "    BoolSeries PreBreakoutFailure" + i.__str__() + "(false);	// 前一次突破是否失败"
    print ""

## Code part
print "Begin"
print "    If(BarStatus == 0)"
print "    {"
for i in range(0, number_of_products):
    print "        FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+\", ExchangeName = \"+Data" + i.__str__() + ".ExchangeName()+ \", ContractSize = \"+Text(Data" + i.__str__() + ".ContractSize()));"
    print "        preEntryPrice" + i.__str__() + " = InvalidNumeric;"
    print "        PreBreakoutFailure" + i.__str__() + " = false;"
    print ""
print "    }"

for i in range(0, number_of_products):
    print "    MinPoint" + i.__str__() + " = Data" + i.__str__() + ".MinMove*Data" + i.__str__() + ".PriceScale;"
    print "    AvgTR" + i.__str__() + " = XAverage(Data" + i.__str__() + ".TrueRange, ATRLength" + i.__str__() + ");"
    print "    N" + i.__str__() + " = AvgTR" + i.__str__() + "[1];"
    print ""
    
print "    TotalEquity = Portfolio_CurrentCapital() + Portfolio_UsedMargin();"

for i in range(0, number_of_products):
    print "    TurtleUnits" + i.__str__() + " = (TotalEquity*RiskRatio" + i.__str__() + "/100) /(N" + i.__str__() + " * Data" + i.__str__() + ".ContractUnit()*Data" + i.__str__() + ".BigPointValue());"
    print "    TurtleUnits" + i.__str__() + " = IntPart(TurtleUnits" + i.__str__() + "); "
    print ""
    print "    DonchianHi" + i.__str__() + " = HighestFC(Data" + i.__str__() + ".High[1], boLength" + i.__str__() + ");"
    print "    DonchianLo" + i.__str__() + " = LowestFC(Data" + i.__str__() + ".Low[1], boLength" + i.__str__() + ");"
    print ""
    print "    fsDonchianHi" + i.__str__() + " = HighestFC(Data" + i.__str__() + ".High[1], fsLength" + i.__str__() + ");"
    print "    fsDonchianLo" + i.__str__() + " = LowestFC(Data" + i.__str__() + ".Low[1], fsLength" + i.__str__() + ");"
    print ""
    print "    ExitLowestPrice" + i.__str__() + " = LowestFC(Data" + i.__str__() + ".Low[1],teLength" + i.__str__() + ");"
    print "    ExitHighestPrice" + i.__str__() + " = HighestFC(Data" + i.__str__() + ".High[1],teLength" + i.__str__() + ");"
    print ""
    print "    FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) + \", N" + i.__str__() +" = \" + Text(N"+ i.__str__() +") + \", preEntryPrice" + i.__str__() +" = \" + Text(preEntryPrice"+ i.__str__() +") + \", preBreakoutFailure" + i.__str__() +" = \" + IIFString(PreBreakoutFailure"+ i.__str__() +",\"True\",\"False\"));"
    print ""
    print "    If(Data" + i.__str__() + ".MarketPosition == 0 && ((!LastProfitableTradeFilter" + i.__str__() + ") Or (PreBreakoutFailure" + i.__str__() + ")))"
    print "    {"
    print "        If(Data" + i.__str__() + ".High > DonchianHi" + i.__str__() + " && TurtleUnits" + i.__str__() + " >= 1)"
    print "        {"
    print "            myEntryPrice" + i.__str__() + " = min(Data" + i.__str__() + ".high, DonchianHi" + i.__str__() + " + MinPoint" + i.__str__() + ");"
    print "            myEntryPrice" + i.__str__() + " = IIF(myEntryPrice" + i.__str__() + " < Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myEntryPrice" + i.__str__() + "); "
    print "            preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "            Data" + i.__str__() + ".Buy(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Open Normal Long Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "            SendOrderThisBar" + i.__str__() + " = True;"
    print "            PreBreakoutFailure" + i.__str__() + " = False;"
    print "        }"
    print "        If(Data" + i.__str__() + ".Low < DonchianLo" + i.__str__() + " && TurtleUnits" + i.__str__() + " >= 1)"
    print "        {"
    print "            myEntryPrice" + i.__str__() + " = max(Data" + i.__str__() + ".low, DonchianLo" + i.__str__() + " - MinPoint" + i.__str__() + ");"
    print "            myEntryPrice" + i.__str__() + " = IIF(myEntryPrice" + i.__str__() + " > Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myEntryPrice" + i.__str__() + ");"
    print "            preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "            SendOrderThisBar" + i.__str__() + " = True;"
    print "            Data" + i.__str__() + ".SellShort(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Open Normal Short Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "            SendOrderThisBar" + i.__str__() + " = True;"
    print "            PreBreakoutFailure" + i.__str__() + " = False;"
    print "        }"
    print "    }"
    print "    If(Data" + i.__str__() + ".MarketPosition == 0)"
    print "    {"
    print "        Commentary(\"fsDonchianHi" + i.__str__() + " = \"+Text(fsDonchianHi" + i.__str__() + "));"
    print "        If(Data" + i.__str__() + ".High > fsDonchianHi" + i.__str__() + " && TurtleUnits" + i.__str__() + " >= 1)"
    print "        {"
    print "            myEntryPrice" + i.__str__() + " = min(Data" + i.__str__() + ".high, fsDonchianHi" + i.__str__() + " + MinPoint" + i.__str__() + ");"
    print "            myEntryPrice" + i.__str__() + " = IIF(myEntryPrice" + i.__str__() + " < Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myEntryPrice" + i.__str__() + "); "
    print "            preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "            Data" + i.__str__() + ".Buy(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Open Longterm Long Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "            SendOrderThisBar" + i.__str__() + " = True;"
    print "            PreBreakoutFailure" + i.__str__() + " = False;"
    print "        }"
    print "        Commentary(\"fsDonchianLo" + i.__str__() + " = \"+Text(fsDonchianLo" + i.__str__() + "));"
    print "        If(Data" + i.__str__() + ".Low < fsDonchianLo" + i.__str__() + " && TurtleUnits" + i.__str__() + " >= 1)"
    print "        {"
    print "            myEntryPrice" + i.__str__() + " = max(Data" + i.__str__() + ".low,fsDonchianLo" + i.__str__() + " - MinPoint" + i.__str__() + ");"
    print "            myEntryPrice" + i.__str__() + " = IIF(myEntryPrice" + i.__str__() + " > Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myEntryPrice" + i.__str__() + "); "
    print "            preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "            Data" + i.__str__() + ".SellShort(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Open Longterm Short Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "            SendOrderThisBar" + i.__str__() + " = True;"
    print "            PreBreakoutFailure" + i.__str__() + " = False;"
    print "        }"
    print "    }"
    print "    If(Data" + i.__str__() + ".MarketPosition == 1)"
    print "    {"
    print "        Commentary(\"ExitLowestPrice" + i.__str__() + " = \" + Text(ExitLowestPrice" + i.__str__() + "));"
    print "        If(Data" + i.__str__() + ".Low < ExitLowestPrice" + i.__str__() + ")    "
    print "        {"
    print "            myExitPrice" + i.__str__() + " = max(Data" + i.__str__() + ".Low, ExitLowestPrice" + i.__str__() + " - MinPoint" + i.__str__() + ");"
    print "            myExitPrice" + i.__str__() + " = IIF(myExitPrice" + i.__str__() + " > Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myExitPrice" + i.__str__() + "); // 大跳空的时候用开盘价代替"
    print "            Data" + i.__str__() + ".Sell(0, myExitPrice" + i.__str__() + ");    // 数量用0的情况下将全部平仓"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Close Long Price = \" + Text(myExitPrice" + i.__str__() + "));"
    print "        }"
    print "        Else"
    print "        {"
    print "            If(preEntryPrice" + i.__str__() + " != InvalidNumeric && TurtleUnits" + i.__str__() + " >= 1)    "
    print "            {"
    print "                If(Data" + i.__str__() + ".Open >= preEntryPrice" + i.__str__() + " + 0.5*N" + i.__str__() + ")    "
    print "                {"
    print "                    myEntryPrice" + i.__str__() + " = Data" + i.__str__() + ".Open;"
    print "                    preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "                    Data" + i.__str__() + ".Buy(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "                    FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Add Long Position Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "                    SendOrderThisBar" + i.__str__() + " = True;"
    print "                }"
    print "                while(Data" + i.__str__() + ".High >= preEntryPrice" + i.__str__() + " + 0.5*N" + i.__str__() + ") "
    print "                {"
    print "                    myEntryPrice" + i.__str__() + " = preEntryPrice" + i.__str__() + " + 0.5 * N" + i.__str__() + ";"
    print "                    preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "                    Data" + i.__str__() + ".Buy(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "                    FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Add Long Position Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "                    SendOrderThisBar" + i.__str__() + " = True;"
    print "                }"
    print "            }"
    print "            If(Data" + i.__str__() + ".Low <= preEntryPrice" + i.__str__() + " - 2 * N" + i.__str__() + " && SendOrderThisBar" + i.__str__() + " == false)"
    print "            {"
    print "                myExitPrice" + i.__str__() + " = preEntryPrice" + i.__str__() + " - 2 * N" + i.__str__() + ";"
    print "                Data" + i.__str__() + ".Sell(0, myExitPrice" + i.__str__() + "); // 数量用0的情况下将全部平仓"
    print "                FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Close(StopLoss) Long Price = \" + Text(myExitPrice" + i.__str__() + "));"
    print "                PreBreakoutFailure" + i.__str__() + " = True;"
    print "            }"
    print "        }"
    print "    }"
    print "    Else If(Data" + i.__str__() + ".MarketPosition ==-1)"
    print "    {"
    print "        Commentary(\"ExitHighestPrice" + i.__str__() + " = \"+Text(ExitHighestPrice" + i.__str__() + "));"
    print "        If(Data" + i.__str__() + ".High > ExitHighestPrice" + i.__str__() + ")"
    print "        {"
    print "            myExitPrice" + i.__str__() + " = Min(Data" + i.__str__() + ".High, ExitHighestPrice" + i.__str__() + " + MinPoint" + i.__str__() + ");"
    print "            myExitPrice" + i.__str__() + " = IIF(myExitPrice" + i.__str__() + " < Data" + i.__str__() + ".Open, Data" + i.__str__() + ".Open, myExitPrice" + i.__str__() + "); // 大跳空的时候用开盘价代替"
    print "            Data" + i.__str__() + ".BuyToCover(0, myExitPrice" + i.__str__() + ");    // 数量用0的情况下将全部平仓"
    print "            FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Close Short Price = \" + Text(myExitPrice" + i.__str__() + "));"
 ##   print "                PreBreakoutFailure" + i.__str__() + " = True;"
    print "        }"
    print "        Else"
    print "        {"
    print "            If(preEntryPrice" + i.__str__() + " != InvalidNumeric && TurtleUnits" + i.__str__() + " >= 1)"
    print "            {"
    print "                If(Data" + i.__str__() + ".Open <= preEntryPrice" + i.__str__() + " - 0.5*N" + i.__str__() + ")"
    print "                {"
    print "                    myEntryPrice" + i.__str__() + " = Data" + i.__str__() + ".Open;"
    print "                    preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "                    Data" + i.__str__() + ".SellShort(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "                    FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Add Short Position Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "                    SendOrderThisBar" + i.__str__() + " = True;"
    print "                }"
    print "                while(Data" + i.__str__() + ".Low <= preEntryPrice" + i.__str__() + " - 0.5 * N" + i.__str__() + ")"
    print "                {"
    print "                    myEntryPrice" + i.__str__() + " = preEntryPrice" + i.__str__() + " - 0.5 * N" + i.__str__() + ";"
    print "                    preEntryPrice" + i.__str__() + " = myEntryPrice" + i.__str__() + ";"
    print "                    Data" + i.__str__() + ".SellShort(TurtleUnits" + i.__str__() + ", myEntryPrice" + i.__str__() + ");"
    print "                    FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Add Short Position Price = \" + Text(myEntryPrice" + i.__str__() + ") + \", Open Long Qty = \" + Text(TurtleUnits" + i.__str__() + "));"
    print "                    SendOrderThisBar" + i.__str__() + " = True;"
    print "                }"
    print "            }"
    print "            If(Data" + i.__str__() + ".High >= preEntryPrice" + i.__str__() + " + 2 * N" + i.__str__() + " &&SendOrderThisBar" + i.__str__() + " == false)"
    print "            {"
    print "                myExitPrice" + i.__str__() + " = preEntryPrice" + i.__str__() + " + 2 * N" + i.__str__() + ";"
    print "                Data" + i.__str__() + ".BuyToCover(0, myExitPrice" + i.__str__() + ");"
    print "                FileAppend(\"C:\\\\TBLog.csv\", \"Symbol " + i.__str__() + " = \"+Data" + i.__str__() + ".Symbol()+ \", DateTime = \" + Text(Data" + i.__str__() + ".Date() + Data" + i.__str__() + ".Time()) +\", Close(StopLoss) Short Price = \" + Text(myExitPrice" + i.__str__() + "));"
    print "                PreBreakoutFailure" + i.__str__() + " = True;"
    print "            }"
    print "        }"
    print "    }"
    print ""
print "End"
