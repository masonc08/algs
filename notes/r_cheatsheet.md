# R Cheatsheet

## Common Libraries
```R
library("caret") # Provides RMSE and CV helpers
library("glmnet") # Provides ridge and lasso regression helpers
library("tidyverse") # Plotting and data manipulation helpers
library("leaps") # Model selection helpers
library("ISLR") # Provides dataset
```


## Basic Operations and Data Manipulation
- `a() %>% b()` is a pipe, equivalent to `b(a())`
- Mutate data, adds or replaces col1 with what it's assigned in the function
  - `data.mutated = mutate(data, col1=ifelse(col1 > 2, 1, 0))`
  - `house.smaller = mutate(house.smaller, multistorey = ifelse(floors >=2, 1, 0))`
- Subset the data based on a condition
  - `data.subset = subset(data, col1 > 2)`
  - `subset(house, price <= 4e6)`
- Group data together by categorical columns and summarize them
  - `group_by(data, col1) %>% summarize()`
- `data$col1 = as.factor(data$col1)` to convert col1 to a categorical variable
  - `house$zipcode = as.factor(house$zipcode)`
- Apply power transformations to input variables with `poly(col1, p)` or `log()`
  ```R
  fit.poly1 <- lm(price ~ I(sqft_living^2), data = house)
  fit.poly2 <- lm(price ~ poly(log(sqft_living),2), data = house)
  fit.poly3 <- lm(price ~ poly(log(sqft_living),3), data = house)
  ```
- `unique(data$col1)` to get all unique values in col1
- `data = na.omit(movies)` to strip `NA` columns


## Regression
- `fit = lm(y ~ x1 + x2 + ... + xn, data=data)` to form a linear model that predicts column y, using columns `x1, x2, ..., xn` in the data
  - column `y` and `x1, x2, ..., xn` must exist in `data` 
  - `fit1 <- lm(price ~ sqft_living, data = house)`
- `fit = lm(y ~ x1 + x1:x2 + x3:x4, data=data)` using `x1:x2` allows two predictors to be used together (multiplicative)
- `fit = lm(y ~ . - y, data=data)` to form linear model that predicts column y using every column but y in the data
- `summary(fit)`, `coef(fit)`
- `predictions = predict(fit, newdata=predicting_data)` to use a model `fit` to predict the outcome of a dataset `predicting_data`
  - if `newdata` is not provided, the predictions of the data used to train the model will be used
- `sigma(fit)` to get root mean squared error (RMSE) of the model's predictions on the training set
- Get RMSE of a set of predictions against a set of actual values
  - `RMSE(predictions, data$actual_output)`
  ```R
  fit1 <- lm(price ~ sqft_living, data = train)
  pred1 <- predict(fit1, newdata=test)
  rmse1 <- RMSE(pred1, test$price)
  ```
- `logreg.fit = glm(y ~ x1 + x2 + ... + xn, data=data, family=binomial())` to fit a logistic regression
- `fit.loess = loess(y ~ x1 + x2 + ... + xn, data=data, span=span)` to build a __locally weighted__ regression with `span` to control the window of points to consider for the weight
  - `span` is an optional parameter
- `fit.robust = rlm(y ~ x1 + x2 + ... + xn, data=data)` to build a __robust__ linear regression


## Cross Validation
- Create a controller for leave-one-out cross validation
  | CV Method                              | Code                                                             |
  |----------------------------------------|------------------------------------------------------------------|
  | Leave-One-Out Cross Validation (LOOCV) | `ctrl = trainControl(method="LOOCV", number=10)`                 |
  | K-Fold Cross Validation                | `ctrl = trainControl(method="cv", number=10)`                    |
  | Repeated Cross Validation              | `ctrl = trainControl(method="repeatedcv", number=10, repeats=5)` |
- Create a __linear__ model with cross validation using a controller `ctrl`
  ```R
  fit <- train(
    form=y ~ x1 + x2 + ... + xn, 
    data=data,
    method="lm",
    trControl=ctrl
  )
  ```
- `predictions = predict(fit, newdata=test)` Predict using the model `fit`, using testing dataset `test`


## Ridge and Lasso Regressions
- Pack input and output variables from dataset `data` into a `model.matrix`
  - `x = model.matrix(y ~ x1 + x2 + ... + xn, data)`
- Obtain optimal value of lambda, use `alpha=1` for lasso regression, `alpha=0` for ridge regression
  - `lambda.optimal = cv.glmnet(x, data$y, alpha=0, nfolds=10)$lambda.min`
  - add optional parameter `family="binomial"` for logistic regression
- Obtain fit
  - `fit = glmnet(x, data$col1, alpha=0, lambda=lambda.optimal)` to create fit using specified regularization
  - add optional parameter `family="binomial"` for logistic regression
- Predict by `predict(fit, newx=model.matrix(y ~ x1 + x2 + ... + xn, data))`
  - apply optional paramter `type="response"` for logistic regression
- `coef(fit)` to obtain all coefficients of model
- Obtain RMSE error by `RMSE(fit, expected_output)`


## Model Selection
- Apply forward or backwards selection using optional parameter `method="forward"` or `method="backward"`
  - `res = regsubsets(y ~ x1 + x2 + ... + xn, data=data, method = "forward", nvmax=ncol(data))`
- Get summary of all selection iterations by `rss = summary(res)`
- Get sum of squared error (RSS) at each iteration by `rss = res$rss`
  - `$rsq` and `$bic` are also available, representing different measures of error
- Find coefficients of model with lowest error by `coef(res, which.min(rss))`


## Plots
- `ggplot(data=data) + ...` produces empty plot, and you and use `+` to add features to the plot
  - `ggplot(data=data) + geom_points(aes(x=col1, y=col2, colour=col3))` to produce a scatterplot of col2 vs col1, categorized by col3
  - `ggplot(data=data) + geom_boxplot(aes(x=col1))` to produce a boxplot on measuring col1
  - `ggplot(data=data) + geom_histogram(aes(x=col1))` to produce a histogram of col1
  - `ggplot(data=data) + geom_density(aes(x=col1))` to produce a line graph of densities of col1
    - This is essentially a histogram but represented by a smooth line
- We can combine multiple graphical attributes by adding them together
  ```R
  ggplot(data = house, aes(x = price)) + 
    geom_histogram(aes(y=..density..), fill='steelblue', alpha=.6, color='grey75') + 
    geom_density()
  ```
- Boxplots of each category `ggplot(data, aes(x=col1, y=col2)) + geom_boxplot()`
  - Create a boxplot for every category in categorical variable col2, measured by col1
  ```R
  house$zipcode <- as.factor(house$zipcode)
    ggplot(house, aes(x=price, y=zipcode, colour=zipcode)) + 
    geom_boxplot() 
  ```


## Snippets
- Build a regression model with dataset `house` and plot it
  ```R
  fit1 <- lm(price ~ sqft_living, data = house)
  preds <- predict(fit)
  ggplot(house, aes(x=sqft_living, y=price)) + 
    geom_point(alpha=.3, size=2) + 
    geom_line(aes(y=preds), colour="blue")
  ```
- Build a 80/20 train-test split with dataset `house`, build a model using train set and find RMSE error against test set
  ```R
  train_size = floor(0.8 * nrow(house))
  train_inds = sample(1:nrow(house), size=train_size)
  train = house[train_inds,] 
  test = house[-train_inds,]
  fit1 = lm(price ~ sqft_living, data = train)
  pred = predict(fit, newdata=test)
  rmse = RMSE(pred1, test$price)
  ```
- Build logistic regression using dataset `Default` and find prediction accuracy
  - We predict the binary column `default`, which consists of `"Yes"` or `"No"`
  ```R
  logreg.fit = glm(default ~ balance + income + student, data=Default, family=binomial())
  probs = predict(logreg.fit, type ='response')
  preds = ifelse(probs >= 0.5, "Yes", "No") # Convert output to "Yes" or "No"
  target = Default$default
  acc = mean(preds == target)
  ```
- Split data into 60/20/20 train-validation-test split using `house` dataset
  ```R
  train_inds = sample(1:nrow(house), size = floor(0.8*nrow(house)))
  train = house[train_inds,]
  test = house[-train_inds,]
  val_inds = sample(1:nrow(train), size = floor(0.25 *nrow(train)))
  val = train[val_inds,]
  train = train[-val_inds,]
  ```
- Train model with k-fold validation on a dataset `train`, predict on a dataset `test`, and measure testing error
  ```R
  ctrl = trainControl(method = "cv", number = 10)
  cv_fit = train(
    form = price ~ poly(sqft_living,10), 
    data = train, 
    method = "lm",
    trControl = ctrl
  )
  fit.p2 = train(form = price ~ poly(sqft_living,2), data = train, method = "lm", trControl = ctrl)
  preds <- predict(fit.p2, newdata=test)
  rmse <- RMSE(preds,test$price)
  ```
- Identify coefficients of model with lowest RSS error using forward selection using dataset `data`
  ```R
  res = regsubsets(varY ~ ., data=data, method = "forward",  nvmax=ncol(data))
  coef(res, which.min(summary(res)$rss))
  ```
- Train logistic ridge regression model on data `train`, predict on data `test`, and measure accuracy
  ```R
  # Model
  x = model.matrix(IsMentalHealthRelated ~ .-IsMentalHealthRelated, train)
  y = train$IsMentalHealthRelated
  lamda.optimal = cv.glmnet(x, y, alpha=0, family="binomial", nfolds=10)$lambda.min
  fit = glmnet(x, y, alpha=0, family="binomial", lambda=lambda.optimal)
  # Prediction and Accuracy
  x = model.matrix(IsMentalHealthRelated ~ .-IsMentalHealthRelated,test)
  probs = predict(fit, newx=x, type='response')
  preds = ifelse(probsl2>= 0.5, 1, 0)
  acc = mean(preds == test$IsMentalHealthRelated) 
  ```
- Batch Gradient Descent Algorithm snippet from assignment 1
  ```R
  BGD <- function(x, y, theta0, alpha = 0.01, epsilon = 1e-8, max_iter=25000){
    # Inputs
    # x      : The input variables (M columns)
    # y      : Output variables    (1 column)
    # theta0 : Initial weight vector (M+1 columns)
    x     <- as.matrix(x)
    y     <- as.matrix(y) 
    N     <- nrow(x)
    i     <- 0
    theta <- theta0
    x     <- cbind(1, x) # Adding 1 as first column for intercept
    imprv <- 1e10
    cost  <- (1/(2*N)) * t(x %*% theta - y) %*% (x %*% theta - y)
    delta <- 1
    while(imprv > epsilon & i < max_iter){cost
      i <- i + 1
      grad <- 0
      for(j in 1:length(y)){
        grad_chng <- x[j, ] * c(y[j]-x[j, ] %*% theta)
        grad <- grad + grad_chng 
      }
      theta <- theta + (alpha / N) * grad
      cost  <- append(cost, (1/(2*N)) * t(x %*% theta - y) %*% (x %*% theta - y))
      imprv <- abs(cost[i+1] - cost[i])
      if((cost[i+1] - cost[i]) > 0) stop("Cost is increasing. Try reducing alpha.")
    }
    print(paste0("Stopped in ", i, " iterations"))
    cost <- cost[-1]
    return(list(theta,cost))
  }
  ```
- Stochastic Gradient Descent Algorithm snippeet from Assignement 1 Solution
  ```R
  SGD <- function(x, y, theta0, alpha = 0.01, epsilon = 1e-8, max_iter=25000){
    # Inputs
    # x      : The input variables (M columns)
    # y      : Output variables    (1 column)
    # theta0 : Initial weight vector (M+1 columns)
    x     <- as.matrix(x)
    y     <- as.matrix(y) 
    N     <- nrow(x)
    i     <- 0
    theta <- theta0
    x     <- cbind(1, x) # Adding 1 as first column for intercept
    imprv <- 1e10
    cost  <- (1/(2*N)) * t(x %*% theta - y) %*% (x %*% theta - y)
    delta <- 1
    while(imprv > epsilon & i < max_iter){
      i <- i + 1
      grad <- 0
      for(j in 1:length(y)){
        grad_chng <- x[j, ] * c(y[j]-x[j, ] %*% theta)
        theta <- theta + (alpha / N) * grad_chng
      }
      cost  <- append(cost, (1/(2*N)) * t(x %*% theta - y) %*% (x %*% theta - y))
      imprv <- abs(cost[i+1] - cost[i])
      if((cost[i+1] - cost[i]) > 0) stop("Cost is increasing. Try reducing alpha.")
    }
    if (i==max_iter){print(paste0("maximum interation ", max_iter, " was reached"))} else {
      print(paste0("Finished in ", i, " iterations"))
    }
    return(list(theta,cost))
  }
  ```
