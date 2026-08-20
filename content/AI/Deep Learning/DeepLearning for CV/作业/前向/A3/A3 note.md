BatchNorm反向传播，注意x的四条路径得到的梯度最后要相加（复制门反向传播的时候梯度相加）
```
        x (N, D)
         │
         ├───────────────┐
         │               │
       mean = μ          │
     (sum / N, dim=0)    │
         │               │
         ▼               │
      xmu = x - μ ◄──────┘
         │
         ├───────────────┐
         │               │
       square            │
         │               │
         ▼               │
      (xmu)^2            │
         │               │
         ▼               │
       var               │
     (sum / N)           │
         │               │
         ▼               │
   var + eps             │
         │               │
         ▼               │
      sqrt               │
         │               │
         ▼               │
     inv_std = 1/std     │
         │               │
         └───────┬───────┘
                 ▼
        x_hat = xmu * inv_std
                 │
                 ▼
                loss
```
