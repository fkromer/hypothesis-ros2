.. _reasoning_:

Reasons for hypothesis-ros2
===========================

*ROS2* and its core packages are designed with security and safety in mind (MISRA conformance, etc.).
(Future) application domains of ROS2 powered systems with security and functional-safety related
requirements imply the need for advanced testing methodologies. *Exemplary Based Testing* is used to
verify specifc control flow paths through software (e.g. the logic of *ROS2* nodes). However it is
not always the best fit for the required extensive testing (of edge cases, etc.).

To increase the faith into the reliability and robustness of such software *Property Based Testing*
and *Fuzzy Testing* are reasonable and community accepted approaches. `hypothesis-ros2`
enables the adaption of *Property Based Testing* and *Fuzzy Testing* to the application level of *ROS2*
powered systems and the implementation of even more powerful test tools (e.g. fully-automated Fuzzers).