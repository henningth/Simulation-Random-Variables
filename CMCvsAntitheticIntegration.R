"
Integration of sqrt(1-x^2) over [0,1] using Crude Monte Carlo (CMC) and antithetic variates.

12.03.2018, H.T.
"

# Parameters
numMCruns <- 250 # Number of CMC evaluations
alpha <- 0.75 # Antithetic split
theta <- pi/4 # Exact result of integrand

# Performance function (which we are integrating over)
"phi" <- function(x)
{
  return( sqrt(1-x^2) )
}

# Generate uniform random numbers and map them accordingly
UnifVec <- runif(numMCruns)
CMCVec <- phi(UnifVec)
AntiVec <- (phi(UnifVec)+phi(1-UnifVec))/2
AntiAlphaVec <- alpha*phi(UnifVec)+(1-alpha)*phi(1-UnifVec)

# Evaluate cumulative estimators
cumsumCMCVec <- cumsum(CMCVec)/rep(1:numMCruns)
cumsumAntiVec <- cumsum(AntiVec)/rep(1:numMCruns)
cumsumAntiAlphaVec <- cumsum(AntiAlphaVec)/rep(1:numMCruns)

# Plots comparison of the estimators
plot(c(1:numMCruns), theta*rep(1,numMCruns), type="l", pch=19, col="blue", xlab="Iteration", ylab="Estimator" )
lines(c(1:numMCruns), cumsumCMCVec, type="l", pch=19, col="red", xlab="Iteration", ylab="Estimator")
lines(c(1:numMCruns), cumsumAntiVec, type="l", pch=19, col="green", xlab="Iteration", ylab="Estimator")
lines(c(1:numMCruns), cumsumAntiAlphaVec, type="l", pch=19, col="magenta", xlab="Iteration", ylab="Estimator")
legend('topright', legend=c("Analytical", "Crude Monte Carlo", "Antithetic", "Alpha-Antithetic"), col=c("blue", "red", "green", "magenta"), lty=1:2, cex=0.8)