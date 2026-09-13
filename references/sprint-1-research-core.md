# Sprint 1 Research Core

Sprint 1 implements the minimum reusable core: scope framing, Research Brief, depth selection, dynamic architecture, evidence/claim tracking, decision and conflict logs, progressive chapter review, chapter state, dependency checks, and recovery from checkpoints.

## Recovery rule

On resume, read `project/state.yaml`, open `active_artifact`, inspect `open_gates`, and continue from the earliest unmet dependency. Never infer completion from a missing artifact.

## State transitions

`brainstorm → brief → architecture → research → writing → reviewing → approved → final`; material problems move a chapter to `reopened`. A project may pause at any state with a checkpoint.
