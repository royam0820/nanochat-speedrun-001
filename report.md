# nanochat training report

Generated: 2025-11-11 09:15:44

## Environment

### Git Information
- Branch: master
- Commit: c6b7ab7 (dirty)
- Message: grad clip logging and printing and cosmetics

### Hardware
- Platform: Linux
- CPUs: 88 cores (176 logical)
- Memory: 944.8 GB
- GPUs: 8x NVIDIA H100 80GB HBM3
- GPU Memory: 633.6 GB total
- CUDA Version: 12.8
- Hourly Rate: $24.00/hour

### Software
- Python: 3.10.12
- PyTorch: 2.8.0+cu128


### Bloat
- Characters: 399,582
- Lines: 9,756
- Files: 48
- Tokens (approx): 99,895
- Dependencies (uv.lock lines): 2,218

Run started: 2025-11-11 09:15:47

---

## Tokenizer training
timestamp: 2025-11-11 09:17:06

- max_chars: 2,000,000,000
- doc_cap: 10,000
- vocab_size: 65,536
- train_time: 69.7707
- num_special_tokens: 9
- token_bytes_min: 1
- token_bytes_max: 32
- token_bytes_mean: 6.9151
- token_bytes_std: 2.8736


## Tokenizer evaluation
timestamp: 2025-11-11 09:17:10

### Comparison with GPT-2

| Text Type | Bytes | GPT-2 Tokens | GPT-2 Ratio | Ours Tokens | Ours Ratio | Relative Diff % |
|-----------|-------|--------------|--------------|-------------|------------|-----------------|
| news | 1819 | 404 | 4.50 | 375 | 4.85 | +7.2% |
| korean | 893 | 745 | 1.20 | 721 | 1.24 | +3.2% |
| code | 1259 | 576 | 2.19 | 493 | 2.55 | +14.4% |
| math | 1834 | 936 | 1.96 | 966 | 1.90 | -3.2% |
| science | 1112 | 260 | 4.28 | 225 | 4.94 | +13.5% |
| fwe-train | 4208518 | 900364 | 4.67 | 856901 | 4.91 | +4.8% |
| fwe-val | 4908443 | 1059062 | 4.63 | 1010356 | 4.86 | +4.6% |

### Comparison with GPT-4

| Text Type | Bytes | GPT-4 Tokens | GPT-4 Ratio | Ours Tokens | Ours Ratio | Relative Diff % |
|-----------|-------|--------------|--------------|-------------|------------|-----------------|
| news | 1819 | 387 | 4.70 | 375 | 4.85 | +3.1% |
| korean | 893 | 364 | 2.45 | 721 | 1.24 | -98.1% |
| code | 1259 | 309 | 4.07 | 493 | 2.55 | -59.5% |
| math | 1834 | 832 | 2.20 | 966 | 1.90 | -16.1% |
| science | 1112 | 249 | 4.47 | 225 | 4.94 | +9.6% |
| fwe-train | 4208518 | 874799 | 4.81 | 856901 | 4.91 | +2.0% |
| fwe-val | 4908443 | 1029691 | 4.77 | 1010356 | 4.86 | +1.9% |


## Base model training
timestamp: 2025-11-11 12:19:38

- run: dummy
- device_type: 
- depth: 20
- max_seq_len: 2048
- num_iterations: -1
- target_flops: -1.0000
- target_param_data_ratio: 20
- device_batch_size: 32
- total_batch_size: 524,288
- embedding_lr: 0.2000
- unembedding_lr: 0.0040
- weight_decay: 0.0000
- matrix_lr: 0.0200
- grad_clip: 1.0000
- warmup_ratio: 0.0000
- warmdown_ratio: 0.2000
- final_lr_frac: 0.0000
- eval_every: 250
- eval_tokens: 10,485,760
- core_metric_every: 2000
- core_metric_max_per_task: 500
- sample_every: 2000
- model_tag: 
- Number of parameters: 560,988,160
- Number of FLOPs per token: 3.491758e+09
- Calculated number of iterations: 21,400
- Number of training tokens: 11,219,763,200
- Tokens : Params ratio: 20.0000
- DDP world size: 8
- warmup_ratio: 0.0000
- warmdown_ratio: 0.2000
- final_lr_frac: 0.0000
- Minimum validation bpb: 0.8120
- Final validation bpb: 0.8120
- CORE metric estimate: 0.2004
- MFU %: 48.04%
- Total training flops: 3.917670e+19
- Total training time: 172.57m
- Peak memory usage: 75422.02MiB


## Base model loss
timestamp: 2025-11-11 12:20:17

- train bpb: 0.8148
- val bpb: 0.8121
- sample 0: <|bos|>The capital of France is Paris. It is the largest city in France and the second largest city in Europe
- sample 1: <|bos|>The chemical symbol of gold is Au. The symbol of gold is Au. The chemical symbol of gold is Au
- sample 2: <|bos|>If yesterday was Friday, then tomorrow will be Thursday. If today is Tuesday, then tomorrow will be Thursday. If today is
- sample 3: <|bos|>The opposite of hot is cold, and cold is hot. The opposite of hot is cold, and cold
- sample 4: <|bos|>The planets of the solar system are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune,
- sample 5: <|bos|>My favorite color is blue. I love the color blue because it is a color that is calming and
- sample 6: <|bos|>If 5*x + 3 = 13, then x is the sum of 3 and 5. If 5*x + 


## Base model evaluation
timestamp: 2025-11-11 12:23:59

- Model: base_model (step 21400)
- CORE metric: 0.1910
- hellaswag_zeroshot: 0.2603
- jeopardy: 0.1063
- bigbench_qa_wikidata: 0.5208
- arc_easy: 0.5264
- arc_challenge: 0.1160
- copa: 0.3400
- commonsense_qa: 0.0551
- piqa: 0.3656
- openbook_qa: 0.1173
- lambada_openai: 0.3714
- hellaswag: 0.2640
- winograd: 0.2821
- winogrande: 0.0639
- bigbench_dyck_languages: 0.1020
- agi_eval_lsat_ar: 0.0272
- bigbench_cs_algorithms: 0.3492
- bigbench_operators: 0.1667
- bigbench_repeat_copy_logic: 0.0000
- squad: 0.2112
- coqa: 0.1987
- boolq: -0.4172
- bigbench_language_identification: 0.1751


## Midtraining
timestamp: 2025-11-11 12:34:01

- run: dummy
- device_type: 
- dtype: bfloat16
- num_iterations: -1
- max_seq_len: 2048
- device_batch_size: 32
- unembedding_lr: 0.0040
- embedding_lr: 0.2000
- matrix_lr: 0.0200
- init_lr_frac: 1.0000
- weight_decay: 0.0000
- eval_every: 150
- eval_tokens: 10,485,760
- total_batch_size: 524,288
- dry_run: 0
- Number of iterations: 809
- DDP world size: 8
- Minimum validation bpb: 0.3953


## Chat evaluation mid
timestamp: 2025-11-11 12:41:50

- source: mid
- task_name: None
- dtype: bfloat16
- temperature: 0.0000
- max_new_tokens: 512
- num_samples: 1
- top_k: 50
- batch_size: 8
- model_tag: None
- step: None
- max_problems: None
- device_type: 
- ARC-Easy: 0.4478
- ARC-Challenge: 0.3311
- MMLU: 0.3315
- GSM8K: 0.0500
- HumanEval: 0.0915
- SpellingBee: 1.0000
- ChatCORE metric: 0.2703


## Chat SFT
timestamp: 2025-11-11 12:44:16

- run: dummy
- source: mid
- device_type: 
- dtype: bfloat16
- device_batch_size: 4
- num_epochs: 1
- num_iterations: -1
- target_examples_per_step: 32
- unembedding_lr: 0.0040
- embedding_lr: 0.2000
- matrix_lr: 0.0200
- weight_decay: 0.0000
- init_lr_frac: 0.0200
- eval_every: 100
- eval_steps: 100
- eval_metrics_every: 200
- eval_metrics_max_problems: 1024
- Training rows: 22,439
- Number of iterations: 701
- Training loss: 0.5317
- Validation loss: 1.0115


## Chat evaluation sft
timestamp: 2025-11-11 12:51:04

- source: sft
- task_name: None
- dtype: bfloat16
- temperature: 0.0000
- max_new_tokens: 512
- num_samples: 1
- top_k: 50
- batch_size: 8
- model_tag: None
- step: None
- max_problems: None
- device_type: 
- ARC-Easy: 0.4684
- ARC-Challenge: 0.3362
- MMLU: 0.3314
- GSM8K: 0.0697
- HumanEval: 0.0915
- SpellingBee: 1.0000
- ChatCORE metric: 0.2793


## Summary

- Characters: 399,582
- Lines: 9,756
- Files: 48
- Tokens (approx): 99,895
- Dependencies (uv.lock lines): 2,218

| Metric          | BASE     | MID      | SFT      | RL       |
|-----------------|----------|----------|----------|----------|
| CORE            | 0.1910   | -        | -        | -        |
| ARC-Challenge   | -        | 0.3311   | 0.3362   | -        |
| ARC-Easy        | -        | 0.4478   | 0.4684   | -        |
| GSM8K           | -        | 0.0500   | 0.0697   | -        |
| HumanEval       | -        | 0.0915   | 0.0915   | -        |
| MMLU            | -        | 0.3315   | 0.3314   | -        |
| ChatCORE        | -        | 0.2703   | 0.2793   | -        |

Total wall clock time: 3h35m
