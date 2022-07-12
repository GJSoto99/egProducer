**Instructions to run the Electron Producer**

First you should run the instructions for the g-doc and produce the output **step0_HLT.root**.

Then run the following commands:
```
cd CMSSW_12_3_5/src
cmsenv
git clone git@github.com:ckoraka/egProducer.git
scram b -j 8
cd egProducer/Producer/test
```

Check in the **eganalyzer_cfg.py** ln.33 that the path to the input root file is the proper one:
```
'file:/path/to/file/step0_HLT.root'
```

then to run do:
```
cmsRun eganalyzer_cfg.py
```
An output named **output.root** should be produced.

