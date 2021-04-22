# Final R Cheatsheet for MSCI 446

## Common Libraries
```R
library("MLmetrics") # LogLoss and Gini index calculators
library("e1071") # PCA
library("tidyverse") # Plotting and data manipulation helpers
library("rpart") # Trees
library("ISLR") # Provides dataset
```

## Decision Trees
- `LogLoss(vct1, vct2)` to measure cross entropy loss between a set of predictions and their actual values
  - used for classification
  - higher is better
- `Gini(vct1, vct2)` to measure gini impurity between a set of predictions and their actual values
  - used for classification
  - lower is better
- `Accuracy(vct1, vct2)`, or `RMSE(vct1, vct2)` for accuracy or RMSE errors, depending on classification or regression
- `tree.model = tree(y ~ x1 + x2 + ..., data=data.train)` to create tree model
  - `plot(tree.model)`, `tree(tree.model)` to plot tree model with branches and texts
- `tree.model = rpart(y ~ x1 + x2 + ..., data=data.train)` to create tre emodel using rpart package
  - same thing as `tree` package, but it does cross validation by default
  - `library('rattle')` and `fancyRpartPlot(tree.model, caption="")` to plot colourful tree
- `preds = predict(tree.model, data.test)` for predictions
- `tree.model.bag = randomForest(y ~ x1 + x2 + ..., data=data.train, mtry=ncol(data.train)-1)` for regular bagging without subsetting predictors
  - `plot(tree.model.bag)` to see a plot of errors vs trees generated off bootstrapping
  - should be an elbow plot
- `tree.model.rforest = randomForest(y ~ x1 + x2 + ..., data=data.train, mtry=preds_amt, importance=T)` for random forest using `preds_amt` of predictors at each branching stage
  - `tree.model.rforest$importance` to identify the most important predictors related to the outcome


## Support Vector Machines
- `svm.model = svm(y ~ x1 + x2 + ..., data=data.train, kernel=kernel_type)`, where `kernel_type` can be `linear`, `radial`, `polynomial`
  - can add parameters `cost=0.05` or `scale=F`
  - `radial` kernels require `gamma=1` parameter in addition to `cost`
- predict by `preds = predict(svm.model, data.test, type="class")`
- plot svm models by `plot(svm.model, data.train)`
- finetune SVMs by trying different cost parameters with CV, to find the model with the best one
  - `svm.model.tuned = tune(svm, y ~ x1 + x2 + ..., kernel=linear, scale=F, ranges=list(cost=c(0.001 , 0.01, 0.1, 1, 5, 10, 100)))$best.model` to find best cost for linear models
  - `svm.model.tuned = tune(svm, y ~ x1 + x2 + ..., kernel=radial, ranges=list(cost=c(0.001 , 0.01, 0.1, 1, 5, 10, 100), gamma=c(0.5, 1, 2, 3, 4)))$best.model` to find best cost and gamma for radial kernels

## Neural Networks
- `nn.model = neuralnet(y ~ x1 + x2 + ..., hidden=c(5, 3), linear.output=F)` for a simple classification neural net
  - `plot(nn.model)` to plot
- `nn.model = keras_model_sequential()` to create empty neural net
- `nn.model %>% layer_dense(units=256, activation='relu', input_shape=c(784)) %>% ... %>% layer_dense(units=10, activation='softmax')` to fill neural net with untrained layers and neurons
  - can also add regularization at any layer by `kernel_regularizer=regularizer_l2(0.001)`, avoids overfitting
  - can also add dropout layers to filter out detected outliers `... %>% layer_dropout(rate=.3) %>% ...`
- `nn.model %>% compile(loss=loss_measure, optimizer=optimizer_adam(), metrics=c('accuracy'))` to compile neural net with specifications
  - `loss_measure` can be different measures, such as `'mean_suared_error'` or `'categorical_crossentropy'`
- `nn.model %>% fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.2)` to train the model with given specification with cross validation using GDA
  - batch_size specifies the gradient batch size
- `nn.model %>% evaluate(x_test, y_test)` to get errors

## Principle Component Analysis
- `pca = prcomp(data[, predictors], scale=T)` to get a linear combination of all predictors for each PCA
  - `dat = data.frame(pca$x)` to cast PCAs into a dataframe
  - `colnames(dat) <- paste0("Ax",1:4)` to name dataframe columns
  - `ggplot(dat, aes(Ax1, Ax2)) + geom_point(alpha=.5)` to plot first two principle components
- see scree plot using `pca$sdev`, shows variation that each component provides
  - if the first two values are high compared to others, then that means plotting on two PCAs is a good description of the data
- `biplot(pca)` to plot biplot

## K-Means Clustering
- `fit = kmeans(data[, predictors], c)` to cluster the `predictors` columns of `data` into `c` clusters
- `table(vct1, vct2)` creates ConfusionMatrix-like table of clusters vs. real classifications

## Hierarchical Clustering
- Compute euclidean distances between a dataframe of points using `dist(data, method="euclidean")`
- Perform hierarchical clustering by `hc = hclust(dists, method=method)`, where `method` can be `"complete"`, `"single"`, `"average"`, `"centroid"`
  - method is how two sets of points are identified after they are merged
  - `plot(hc)` to plot dendrogram
- `clus = cutree(hc, k=k)` to slice tree down to `k` subgroups
- `plot(hc, labels=clus)` to display sliced dendrogram

## Functions
- train test split
```R
ttsplit = function(x, train_split=.8) {
  train_ind = sample(1:nrow(x), floor(train_split*nrow(x)))
  train = x[train_ind, ]
  test = dat[-train_ind, ]
  list(train=train, test=test)
}
```

## Snippets
- train tree using `tree` package and cross validate it with penalty parameter added to gini index
```R
library('tree')
bc.tree <- tree(Classification ~ ., data=bc)
cv <- cv.tree(bc.tree, FUN = prune.misclass)
best <- cv$size[which.min(dev)]
bc.tree.pruned <- prune.misclass(bc.tree,best=best)
```
- train tree using `rpart`, predict classifications, create `ConfusionMatrix`
```R
bc.tree <- rpart(Classification ~ ., data=bc)
preds   <- predict(bc.tree, type = "class") # remove class if not classifying
ConfusionMatrix(preds, bc$Classification)
Gini(preds, bc$Classification)
LogLoss(preds, bc$Classification)
Accuracy(preds, bc$Classification)
```
- linear SVM kernel
```R
svmfit <- svm(y ~ x1+x2, data=dat , kernel ="linear", cost =0.05,scale =FALSE)
preds <- predict(svmfit,dat, type="class")
```
- linear SVM kernel with finetuning for cost
```R
tune.out <- tune(svm ,y~.,data=dat ,kernel ="linear",scale =FALSE,
              ranges =list(cost=c(0.001 , 0.01, 0.1, 1,5,10,100) ))
bestmod <- tune.out$best.model
preds   <- predict(bestmod,dat[,1:2], type="class")
```
- radial SVM kernel with finetuning for gamma and cost
```R
tune.out <- tune(svm, y~., data=dat, kernel ="radial",
              ranges =list(cost=c(0.01, 0.05, .1 ,1 ,10 ,100 ,1000),
                           gamma=c(0.5,1,2,3,4)))
preds.svmCV <- predict(tune.out$best.model,dat)
```
- make empty NN, train it, then evaluate error
```R
model <- keras_model_sequential() 
model %>% 
  layer_dense(units = 256, activation = 'relu', input_shape = c(784)) %>% 
  layer_dense(units = 128, activation = 'relu') %>%
  layer_dense(units = 10, activation = 'softmax')
model %>% compile(
  loss = 'categorical_crossentropy',
  optimizer = optimizer_adam(), # gradient descent
  metrics = c('accuracy')
)
model %>% fit(
  x_train, y_train, 
  epochs = 10, batch_size = 128, 
  validation_split = 0.2
)
model %>% evaluate(x_test, y_test)
```
- make NN with l2 regularization in a hidden layer, train it, then evaluate error
```R
model <- keras_model_sequential() 
model %>% 
  layer_dense(units = 256, activation = 'relu', input_shape = c(784)) %>% 
  layer_dense(units = 128, activation = 'relu', kernel_regularizer = regularizer_l2(0.001)) %>% 
  layer_dense(units = 10, activation = 'softmax')
model %>% compile(
  loss = 'categorical_crossentropy',
  optimizer = optimizer_adam(),
  metrics = c('accuracy')
)
history <- model %>% fit(
  x_train, y_train, 
  epochs = 20, 
  batch_size = 128, 
  validation_split = 0.2
)
model %>% evaluate(x_test, y_test)
```
- make NN with dropout layer, train it, then evaluate error
```R
model <- keras_model_sequential() 
model %>% 
  layer_dense(units = 256, activation = 'relu', input_shape = c(784)) %>% 
  layer_dense(units = 128, activation = 'relu') %>% 
  layer_dropout(rate = 0.3) %>% 
  layer_dense(units = 10, activation = 'softmax')
model %>% compile(
  loss = 'categorical_crossentropy',
  optimizer = optimizer_adam(),
  metrics = c('accuracy')
)
history <- model %>% fit(
  x_train, y_train, 
  epochs = 10, 
  batch_size = 128, 
  validation_split = 0.2
)
model %>% evaluate(x_test, y_test)
```
- Find optimal PCA for a dataset and plot it
```R
pca <- prcomp(iris[,1:4], scale = TRUE)
dat <- data.frame(pca$x)
colnames(dat) <- paste0("Ax",1:4)
ggplot(dat, aes(Ax1, Ax2)) + 
  geom_point(alpha=.5)
pca
```
- Cluster data by k-means and plot it, then compute ConfusionMatrix
```R
fit <- kmeans(iris[,1:4],3)
clus <- as.factor(fit$cluster)
ggplot(iris, aes(x=Sepal.Length, y=Petal.Width, colour=clus)) + 
  geom_point(alpha=.5, size =2)
table(iris$Species, clus)
```
- Compute dendrogram using `"average"` identifier, then slice it to 2 subgroups and plot the sliced dendrogram
```R
dists <- dist(mtcars[,1:7],method = "euclidean")
hc.average  <- hclust(dists, method="average")
clus <- cutree(hc.average,  k=2)
plot(hc.average, labels = clus)
```

## Sources and Further References
1. [Tutorial 8, Trees & Forests](https://braininamath.github.io/TheStory/W8_Trees.html)
2. [Tutorial 9, Support Vector Machines](https://braininamath.github.io/TheStory/W9_SVM.html)
3. [Tutorial 10, Neural Networks in R](https://braininamath.github.io/TheStory/W10_NNets.html)
4. [Tutorial 11, Neural Networks in R, cont.](https://braininamath.github.io/TheStory/W11_NNets.html)
5. [Tutorial 12, Principle Component Analysis](https://braininamath.github.io/TheStory/W12_PCA.html)
6. [Tutorial 13, Unsupervised Learning](https://braininamath.github.io/TheStory/W13_Kmeans.html)
7. [Assignment 3](https://learn.uwaterloo.ca/d2l/le/content/655854/viewContent/3581175/View)
8. [Assignment 4](https://learn.uwaterloo.ca/d2l/le/content/655854/viewContent/3624972/View)
