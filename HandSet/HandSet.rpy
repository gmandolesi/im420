I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID 7e097a38-24a6-4965-b8eb-7d7cbc118550;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 1;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "HandSet";
	- _objectCreation = "261810927522018142135326";
	- _umlDependencyID = "2267";
	- _lastID = 3;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "RequerimentsPkg.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "RequerimentsPkg";
		- _id = GUID 991b61e8-6659-4719-8375-c1bc0065fa34;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 05af3d41-1fae-426d-9d6d-9cfdcb83445a;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 13;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ ISubsystem 
			- fileName = "RequerimentsPkg";
			- _id = GUID 991b61e8-6659-4719-8375-c1bc0065fa34;
		}
		{ ISubsystem 
			- fileName = "AnalysisPkg";
			- _id = GUID b297d0d9-e88d-44eb-8a12-b3470d218dc3;
		}
		{ ISubsystem 
			- fileName = "ArchitecturePkg";
			- _id = GUID 6f821f85-2563-43a5-8e51-0841792b23eb;
		}
		{ ISubsystem 
			- fileName = "SubsystemsPkg";
			- _id = GUID 9d00d6df-d4dc-4e61-808b-1834d9563489;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID e2647990-e8f5-418e-9235-05a9093662b4;
			- _myState = 8192;
			- _name = "Model1";
			- _objectCreation = "261811127522018142133326";
			- _umlDependencyID = "2125";
			- _lastModifiedTime = "3.20.2018::17:33:54";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 774e227f-6557-4714-93b6-d903a93ee9ff;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID e2647990-e8f5-418e-9235-05a9093662b4;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 1;
				{ CGIClass 
					- _id = GUID 4386810d-1ba2-4647-bbab-3bde778880a6;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "RequerimentsPkg.sbs";
						- _subsystem = "RequerimentsPkg";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 7bcff239-a9a3-4202-8be3-f0d952a780bf;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 4386810d-1ba2-4647-bbab-3bde778880a6;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "RequerimentsPkg.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "RequerimentsPkg";
				- _id = GUID 991b61e8-6659-4719-8375-c1bc0065fa34;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 05af3d41-1fae-426d-9d6d-9cfdcb83445a;
		}
	}
}

