{'loss': 1.6669, 'learning_rate': 1.6941080838585537e-05, 'epoch': 0.99}                                                
{'loss': 1.652, 'learning_rate': 1.6867867656192946e-05, 'epoch': 1.0}                                                  
 33%|█████████████████████████▎                                                  | 575/1725 [3:03:39<6:06:20, 19.11s/it[rank1]:[E ProcessGroupNCCL.cpp:523] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=1505645, OpType=_ALLGATHER_BASE, NumelIn=14680064, NumelOut=29360128, Timeout(ms)=1800000) ran for 1800410 milliseconds before timing out.
[rank0]:[E ProcessGroupNCCL.cpp:523] [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=1505766, OpType=ALLGATHER, NumelIn=8, NumelOut=16, Timeout(ms)=1800000) ran for 1800238 milliseconds before timing out.
[rank0]:[E ProcessGroupNCCL.cpp:537] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank0]:[E ProcessGroupNCCL.cpp:543] To avoid data inconsistency, we are taking the entire process down.
[rank0]:[E ProcessGroupNCCL.cpp:1182] [Rank 0] NCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=1505766, OpType=ALLGATHER, NumelIn=8, NumelOut=16, Timeout(ms)=1800000) ran for 1800238 milliseconds before timing out.
Exception raised from checkTimeout at ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:525 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f610c181d87 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e6 (0x7f60c149c6e6 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::workCleanupLoop() + 0x19d (0x7f60c149fc3d in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x119 (0x7f60c14a0839 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc463 (0x7f610b6dc463 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x883ec (0x7f610cf6a3ec in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x108a4c (0x7f610cfeaa4c in /lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [Rank 0] NCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=1505766, OpType=ALLGATHER, NumelIn=8, NumelOut=16, Timeout(ms)=1800000) ran for 1800238 milliseconds before timing out.
Exception raised from checkTimeout at ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:525 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f610c181d87 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e6 (0x7f60c149c6e6 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::workCleanupLoop() + 0x19d (0x7f60c149fc3d in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x119 (0x7f60c14a0839 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc463 (0x7f610b6dc463 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x883ec (0x7f610cf6a3ec in /lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x108a4c (0x7f610cfeaa4c in /lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1186 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f610c181d87 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xdf6b11 (0x7f60c11f6b11 in /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xdc463 (0x7f610b6dc463 in /lib/x86_64-linux-gnu/libstdc++.so.6)
frame #3: <unknown function> + 0x883ec (0x7f610cf6a3ec in /lib/x86_64-linux-gnu/libc.so.6)
frame #4: <unknown function> + 0x108a4c (0x7f610cfeaa4c in /lib/x86_64-linux-gnu/libc.so.6)

[2024-03-12 02:29:19,487] torch.distributed.elastic.multiprocessing.api: [WARNING] Sending process 48241 closing signal SIGTERM
[2024-03-12 02:29:19,601] torch.distributed.elastic.multiprocessing.api: [ERROR] failed (exitcode: -6) local_rank: 0 (pid: 48240) of binary: /home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/bin/python3.11
Traceback (most recent call last):
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/bin/accelerate", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/accelerate/commands/accelerate_cli.py", line 47, in main
    args.func(args)
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/accelerate/commands/launch.py", line 1008, in launch_command
    deepspeed_launcher(args)
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/accelerate/commands/launch.py", line 724, in deepspeed_launcher
    distrib_run.run(args)
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/distributed/run.py", line 803, in run
    elastic_launch(
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/distributed/launcher/api.py", line 135, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/venv/lib/python3.11/site-packages/torch/distributed/launcher/api.py", line 268, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
/home/jotschi/workspaces/ml/lavis-experiments/mistral-deepspeed/sft_trainer_4bit.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-03-12_02:29:19
  host      : plexus.sky
  rank      : 0 (local_rank: 0)
  exitcode  : -6 (pid: 48240)
  error_file: <N/A>
  traceback : Signal 6 (SIGABRT) received by PID 48240
============================================================
(venv) jotschi@plexus ~/workspaces/ml/lavis-experiments/mistral-deepspeed[master]$ 
(venv) jotschi@plexus ~/workspaces/ml/lavis-experiments/mistral-deepspeed[master]$ 
