library(readr)
resultado <- read_csv("ProbabilisticPlanning-master/analises/resultado")

library(ggplot2)

temposLao<-resultado[resultado$algoritmo=='LAO' & resultado$tipoState=='DeterministicGoalState',]
temposIter<- resultado[resultado$algoritmo=='ITER'  & resultado$tipoState=='DeterministicGoalState',]

ggplot() + 
  geom_line(data = temposLao, aes(x = 1:10, y = tempo), color = "darkblue",size=1.1) +
  geom_line(data = temposIter,aes(x = 1:10, y = tempo), color = "orange",size=1.1) +
  xlab('Número do problema') + ylab('Tempo') + ggtitle('Deterministic Goal State')+
  scale_x_continuous(breaks=1:10)

temposLao<-resultado[resultado$algoritmo=='LAO' & resultado$tipoState=='RandomGoalState',]
temposIter<- resultado[resultado$algoritmo=='ITER'  & resultado$tipoState=='RandomGoalState',]

ggplot() + 
  geom_line(data = temposLao, aes(x=1:10, y = tempo), color = "darkblue",size=1.1) +
  geom_line(data = temposIter,aes(x =1:10, y = tempo), color = "orange",size=1.1) +
  xlab('Número do problema') + ylab('Tempo') + ggtitle('Random Goal State')+
  scale_x_continuous(breaks=1:10)
