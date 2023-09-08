# Inledning

Maskininlärning har blivit en kraftfull teknik för att förutsäga och modellera olika fenomen. En av de mest grundläggande maskininlärningsalgoritmerna är linjär regression, som används för att förutsäga huspriser baserat på olika egenskaper. Denna rapport kommer att utforska de olika stegen i en maskininlärningsapplikation som använder linjär regression för att förutspå huspriser och diskutera de teknologier som kan användas i varje steg.

## Datainsamling

Alla maskininlärningsprojekt börjar med datainsamling. Datainsamlingen beror mycket på projektets mål och kan involvera insamling från filer, databaser eller till och med webbskrapning av fastighetswebbplatser. I fallet med att förutspå huspriser behöver vi data som beskriver husens egenskaper, storlek, pris med mera. Denna data kan samlas in från olika källor, inklusive offentliga register, fastighetsmäklare och onlineplattformar [^1]. När datan har samlats in måste den lagras och struktureras på rätt sätt för att vara användbar i modelleringen.

## Datavisualisering

Genom visualisering kan vi förstå data och dess mönster. Det hjälper också att förbereda data för modellering. Man kan använda verktyg som Matplotlib, ett Python-bibliotek, för att skapa olika typer av diagram som linjediagram, stapeldiagram och mer [^2]. Det är viktigt att identifiera vilka variabler och egenskaper i datan som ska visualiseras. Beroende på dataområdet kan olika diagram och visualiseringar vara användbara, inklusive histogram för fördelningen av enskilda variabler, spridningsdiagram för att visa samband mellan variabler och kartor för geografiska data.

## Datarengöring

Efter datainsamlingen är det nödvändigt att rengöra datan genom att hitta och hantera saknade värden och felaktiga poster. Det innebär att man tar bort dubbletter, hanterar saknade värden och rättar till felaktig data. Data som innehåller kategorisk information, såsom husets typ (till exempel "enfamiljshus" eller "lägenhet"), måste omvandlas till numeriska värden. Därefter behöver man skapa en matris där varje rad representerar ett hus och varje kolumn en egenskap. Denna process organiserar data i rätt format för modellträning.

## Linjär Regression

Linjär regression används för att förutsäga huspriser genom att hitta en linjär relation mellan egenskaper som antal rum, geografiskt läge och husstorlek och priserna på husen. Modellen tränas med historisk data för att förstå hur dessa egenskaper påverkar priserna [^3]. När modellen är tränad kan den användas för att göra prisprognoser för nya hus baserat på deras egenskaper.

## Modellträning och Utvärdering

Modellträning börjar med datainsamling och rengöring, följt av val av de mest relevanta egenskaperna. Sedan skapas en linjär modell som försöker hitta mönster mellan de valda egenskaperna och huspriserna. Modellen tränas med hjälp av data för att förstå hur egenskaperna påverkar priserna. Slutligen utvärderas modellens prestanda genom att testa dess förmåga att förutsäga priser med data som den inte tidigare har sett.

## Driftsättning av Modellen

Modellen måste göras redo för användning utanför träningsmiljön. Det innebär att skapa ett gränssnitt, vanligtvis ett API, för att integrera modellen i produktionssystemet och göra realtidsförutsägelser. Det är viktigt att övervaka modellens prestanda i produktionen och uppdatera den vid behov.

## Teknologier

För att samla in data kan tekniker som SQL och webbskrapning användas. För datavisualisering är Matplotlib och Jupyter Notebook användbara verktyg. Modellträning kan utföras med hjälp av Scikit-Learn, Keras och Tensorflow. Vid databearbetning är pandas och numpy användbara, och för driftsättning finns teknologier som Docker, Kubernetes och API-ramverk som Flask och FastAPI.

## Referenser

1.https://towardsdatascience.com/workflow-of-a-machine-learning-project-ec1dba419b94

2. https://www.machinelearningplus.com/machine-learning/linear-regression-in-machine-learning/

3. https://medium.com/codex/how-to-collect-data-for-a-machine-learning-model-2b152752a15b

4. The Statquest Illustrated Guide To Machine Learning(bok).

5. How Ai Works, by Ronald T. Kneusel(ebook)

