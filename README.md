Lady Clucksworth Vs The World
===========================

Simple learner project for Python based on original code from <https://github.com/orkslayergamedev/python-classes-text-battle>

The sky is falling! The weasels are attacking! The raccoons are stealing food! The dog is asleep! EEEEEK!!

It is up to YOU to guide Lady Clucksworth, a somewhat delusional and overly self-important hen of a typical country farm, in her attempts to stave off Certain Doom for herself and her farm-yard friends by dealing with a variety of problems, both real and imagined.

## Class dependencies
Map.name
Map.scene_settings ->   Grid.current_location ->    Location.name
                                                    Location.description
                                                    Location.lore
                        Grid.connects_to -> Bridge.description
                                            Bridge.links_to ->  Location.name
                                                                Location.description
                                                                Location.lore
