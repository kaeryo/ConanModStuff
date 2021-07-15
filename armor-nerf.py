import re

#itemtable must be split to smaller pieces
tableOutput = open("armornerf.txt", "a")

tableOutput.write("---,Name,ShortDesc,LongDesc,Icon,IconLayers,ItemClass,BuildingClass,VisualObject,ActionBlueprint_Use,MaxStackSize,EquipLocation,GUICategory,ItemTags,ArmourValue,")
tableOutput.write("ArmorType,SoundPhysicalSurface,WeaponType,WeaponArcheType,CompatableAmmunitions,SoundTransmitterType,KnockbackResponseWeapon,WeaponStaminaAttackSingleBasic,")
tableOutput.write("WeaponStaminaAttackSingleSpecial,WeaponStaminaAttackDualBasic,WeaponStaminaAttackDualSpecial,WeaponStaminaHeavyChargedRegenModifier,WeaponSpeedHeavyChargedModifier,")
tableOutput.write("EncumbranceWeight,ConeAngle,ConeMaxDistance,DamageHealthLight_OnHit,DamageHealthHeavy_OnHit,DamageStaminaLight_OnHit,DamageStaminaHeavy_OnHit,DamageHealthLight_OnBlock,")
tableOutput.write("DamageHealthHeavy_OnBlock,DamageStaminaLight_OnBlock,DamageStaminaHeavy_OnBlock,HarvestDamage,WeaponUsage,MaxAttackReach,MinAttackReach,MinAttackDistance,WeaponEffectWidth,")
tableOutput.write("WeaponEffectHeight,ItemTier,ArmorPen,DamageConcussiveLightOnHit,DamageConcussiveHeavyOnHit,DamageConcussiveLightOnBlock,DamageConcussiveHeavyOnBlock,DamageTier,CoolDownTime,")
tableOutput.write("ReuseTime,SelectionWeight,KnockbackOffenseBasic,KnockbackOffenseSpecial,KnockbackOffenseBasicOnBlock,KnockbackOffenseSpecialOnBlock,KnockbackDefense,VisualStaticMesh,")
tableOutput.write("VisualSkeletalMesh,VisualDestructibleMesh,WeaponStatusDefault,WeaponStatusCurrent,WeaponStatusDecrement,PerishRate,PerishTo,MaxDurability,RepairItem1,")
tableOutput.write("RepairItem1_Amount,RepairItem1_Weight,RepairItem2,RepairItem2_Amount,RepairItem2_Weight,RepairItem3,RepairItem3_Amount,RepairItem3_Weight,AffectedByDamageTiers,")
tableOutput.write("BuildingPieceScore,BuildingMaxHealth,RepairXP,FirstModifier,SecondModifier,ThirdModifier,FourthModifier,FoodAmount,DrinkAmount,BurnTime,ItemFlags,ItemContainerSize,")
tableOutput.write("AvatarType,DyeColourID,WarPaintID,StaminaCostMultiplier,StaminaClimbingCostMultiplier,LeavesGhostItem,DLCPackage,SpawnTemplateID\n")

for i in range(1,7):
    with open(str(i)+".txt") as tableInput:
        for line in tableInput:
            if re.search('"None","1","3","Armor",""',line): #helmet
                editedVersion = re.sub('"\/Game\/Items\/.*","None","\/Game\/Items\/GatheringResources\/Rock1.Rock1_C"','"/Game/Items/BPGameItemArmor.BPGameItemArmor_C","None","/Game/Items/GatheringResources/Rock1.Rock1_C"',line)
                if re.search('"Armor","","([1|[6-9]|[1-9][0-9][0-9])\.000000","10"',editedVersion): #light that needs nerf
                    editedVersion = re.sub('"Armor","","([1][6-9]|[1-9][0-9][0-9])\.000000","10"','"Armor","","16\.000000","10"',editedVersion)
                if re.search('"Armor","","([6-9][0-9]|[1-9][0-9][0-9])\.000000","75"',editedVersion): #medium that needs nerf
                    editedVersion = re.sub('"Armor","","([6-9][0-9]|[1-9][0-9][0-9])\.000000","75"','"Armor","","67\.000000","75"',editedVersion)
                if re.search('"Armor","","([1][6-9][0-9]|[2-9][0-9][0-9])\.000000","1000"',editedVersion): #heavy that needs nerf
                    editedVersion = re.sub('"Armor","","([1][6-9][0-9]|[2-9][0-9][0-9])\.000000","1000"','"Armor","","160\.000000","1000"',editedVersion)
                tableOutput.write(editedVersion)
            
            if re.search('"None","1","4","Armor",""',line): #chest
                editedVersion = re.sub('"\/Game\/Items\/.*","None","\/Game\/Items\/GatheringResources\/Rock1.Rock1_C"','"/Game/Items/BPGameItemArmor.BPGameItemArmor_C","None","/Game/Items/GatheringResources/Rock1.Rock1_C"',line)
                if re.search('"Armor","","([2-9][0-9]|[1-9][0-9][0-9])\.000000","10"',editedVersion): #light that needs nerf
                    editedVersion = re.sub('"Armor","","([2-9][0-9]|[1-9][0-9][0-9])\.000000","10"','"Armor","","28\.000000","10"',editedVersion)
                if re.search('"Armor","","([1][1-9][0-9]|[2-9][0-9][0-9])\.000000","75"',editedVersion): #medium that needs nerf
                    editedVersion = re.sub('"Armor","","([1][1-9][0-9]|[2-9][0-9][0-9])\.000000","75"','"Armor","","118\.000000","75"',editedVersion)
                if re.search('"Armor","","([2][8-9][0-9]|[3-9][0-9][0-9])\.000000","1000"',editedVersion): #heavy that needs nerf
                    editedVersion = re.sub('"Armor","","([2][8-9][0-9]|[3-9][0-9][0-9])\.000000","1000"','"Armor","","280\.000000","1000"',editedVersion)
                tableOutput.write(editedVersion)
            
            if re.search('"None","1","5","Armor",""',line): #glove
                editedVersion = re.sub('"\/Game\/Items\/.*","None","\/Game\/Items\/GatheringResources\/Rock1.Rock1_C"','"/Game/Items/BPGameItemArmor.BPGameItemArmor_C","None","/Game/Items/GatheringResources/Rock1.Rock1_C"',line)
                if re.search('"Armor","","([8-9]|[1-9][0-9]|[1-9][0-9][0-9])\.000000","10"',editedVersion): #light that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9]|[1-9][0-9]|[1-9][0-9][0-9])\.000000","10"','"Armor","","8\.000000","10"',editedVersion)
                if re.search('"Armor","","([3-9][0-9]|[1-9][0-9][0-9])\.000000","75"',editedVersion): #medium that needs nerf
                    editedVersion = re.sub('"Armor","","([3-9][0-9]|[1-9][0-9][0-9])\.000000","75"','"Armor","","34\.000000","75"',editedVersion)
                if re.search('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","1000"',editedVersion): #heavy that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","1000"','"Armor","","80\.000000","1000"',editedVersion)
                tableOutput.write(editedVersion)
            
            if re.search('"None","1","6","Armor",""',line): #pants
                editedVersion = re.sub('"\/Game\/Items\/.*","None","\/Game\/Items\/GatheringResources\/Rock1.Rock1_C"','"/Game/Items/BPGameItemArmor.BPGameItemArmor_C","None","/Game/Items/GatheringResources/Rock1.Rock1_C"',line)
                if re.search('"Armor","","([2-9][0-9]|[1-9][0-9][0-9])\.000000","10"',editedVersion): #light that needs nerf
                    editedVersion = re.sub('"Armor","","([2-9][0-9]|[1-9][0-9][0-9])\.000000","10"','"Armor","","20\.000000","10"',editedVersion)
                if re.search('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","75"',editedVersion): #medium that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","75"','"Armor","","84\.000000","75"',editedVersion)
                if re.search('"Armor","","([2-9][0-9][0-9])\.000000","1000"',editedVersion): #heavy that needs nerf
                    editedVersion = re.sub('"Armor","","([2-9][0-9][0-9])\.000000","1000"','"Armor","","200\.000000","1000"',editedVersion)
                tableOutput.write(editedVersion)
            
            if re.search('"None","1","7","Armor",""',line): #boots
                editedVersion = re.sub('"\/Game\/Items\/.*","None","\/Game\/Items\/GatheringResources\/Rock1.Rock1_C"','"/Game/Items/BPGameItemArmor.BPGameItemArmor_C","None","/Game/Items/GatheringResources/Rock1.Rock1_C"',line)
                if re.search('"Armor","","([8-9]|[1-9][0-9]|[1-9][0-9][0-9])\.000000","10"',editedVersion): #light that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9]|[1-9][0-9]|[1-9][0-9][0-9])\.000000","10"','"Armor","","8\.000000","10"',editedVersion)
                if re.search('"Armor","","([3][4-9]|[4-9][0-9]|[1-9][0-9][0-9])\.000000","75"',editedVersion): #medium that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","75"','"Armor","","34\.000000","75"',editedVersion)
                if re.search('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","1000"',editedVersion): #heavy that needs nerf
                    editedVersion = re.sub('"Armor","","([8-9][0-9]|[1-9][0-9][0-9])\.000000","1000"','"Armor","","80\.000000","1000"',editedVersion)
                tableOutput.write(editedVersion)