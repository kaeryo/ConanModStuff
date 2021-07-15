import re

#itemtable must be split to smaller pieces
tableOutput = open("weaponnerf.txt", "a")

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
            if re.search("\/Game\/Items\/Weapons\/Sword1h\/sword1h",line):
                removeSpecialEffect = re.sub('\/Game\/Items\/BPGameItemWeapon.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","45","45","0","0","45","45","45","45","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.076500","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)
    
            if re.search("/Game/Items/Weapons/Axe/axe1h",line): #axe changes
                removeSpecialEffect = re.sub('/Game/Items/BPGameItemWeapon_.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","48","48","0","0","48","48","48","48","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.000000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Club/BP_club_1h",line): #mace changes
                removeSpecialEffect = re.sub('/Game/Items/BPGameItemWeapon_.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","45","45","0","0","45","45","45","45","0",',removeSpecialEffect)
                lowerArpen = re.sub('"4(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.229500","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Spear/BP_spear_1h",line): #javelin changes
                removeSpecialEffect = re.sub('/Game/Items/BP_ProjectileWeaponThrown_.*?"','/Game/Items/BP_ProjectileWeaponThrown.BP_ProjectileWeaponThrown_C"',line)
                lowerDamage = re.sub('"250\.000000","[5-9]\d","[5-9]\d","0","0","[5-9]\d","[5-9]\d","[5-9]\d","[5-9]\d","0",','"250.000000","50","50","0","0","50","50","50","50","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.153000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Swordshort/BP_Base_Visual_Swordshort",line): #short sword changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Swordshort/BP_Base_Item_Swordshort_.*?"','/Game/Items/Weapons/Swordshort/BP_Base_Item_Swordshort.BP_Base_Item_Swordshort_C"',line)
                lowerDamage = re.sub('"250\.000000","[5-9]\d","[5-9]\d","0","0","[5-9]\d","[5-9]\d","[5-9]\d","[5-9]\d","0",','"250.000000","56","56","0","0","56","56","56","56","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.153000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Dagger_Offhand/BP_dagger_dw",line): #daggers changes
                removeSpecialEffect = re.sub('/Game/Items/BPGameItemWeapon_.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","39","39","0","0","39","39","39","39","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.153000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Axe2h/BP_Base_Visual_Axe2h",line): #greataxe changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Axe2h/BP_Base_Item_Axe2h_.*?"','/Game/Items/Weapons/Axe2h/BP_Base_Item_Axe2h.BP_Base_Item_Axe2h_C"',line)
                lowerDamage = re.sub('"250\.000000","[6-9]\d","[6-9]\d","0","0","[6-9]\d","[6-9]\d","[6-9]\d","[6-9]\d","0",','"250.000000","67","67","0","0","67","67","67","67","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.000000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Maul2h/BP_maul_2h",line): #warhammer changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Maul2h/BP_Item_MaulBase_.*?"','/Game/Items/Weapons/Maul2h/BP_Item_MaulBase.BP_Item_MaulBase_C"',line)
                lowerDamage = re.sub('"250\.000000","[5-9]\d","[5-9]\d","0","0","[5-9]\d","[5-9]\d","[5-9]\d","[5-9]\d","0",','"250.000000","50","50","0","0","50","50","50","50","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.267750","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Spear2h/BP_spear_2h",line): #spear changes
                removeSpecialEffect = re.sub('/Game/Items/BPGameItemWeapon_.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","45","45","0","0","45","45","45","45","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.076500","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Sword2h/sword2h",line): #greatsword changes
                removeSpecialEffect = re.sub('/Game/Items/BPGameItemWeapon_.*?"','/Game/Items/BPGameItemWeapon.BPGameItemWeapon_C"',line)
                lowerDamage = re.sub('"250\.000000","[5-9]\d","[5-9]\d","0","0","[5-9]\d","[5-9]\d","[5-9]\d","[5-9]\d","0",','"250.000000","56","56","0","0","56","56","56","56","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.191250","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)
    
            if re.search("/Game/Items/Weapons/Katana2h/katana2h",line): #katana changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Katana2h/BP_Item_KatanaBase_.*?"','/Game/Items/Weapons/Katana2h/BP_Item_KatanaBase.BP_Item_KatanaBase_C"',line)
                lowerDamage = re.sub('"250\.000000","[4-9]\d","[4-9]\d","0","0","[4-9]\d","[4-9]\d","[4-9]\d","[4-9]\d","0",','"250.000000","48","48","0","0","48","48","48","48","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.114750","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Bow/BP_bow_2h",line): #bow changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Bow/BP_Item_BowLauncherHyrkanian.*?"','/Game/Items/Weapons/Bow/BP_Item_BowLauncherHyrkanian.BP_Item_BowLauncherHyrkanian_C"',line)
                lowerDamage = re.sub('"250\.000000","[2-9]\d","[2-9]\d","0","0","[2-9]\d","[2-9]\d","[2-9]\d","[2-9]\d","0",','"250.000000","20","20","0","0","20","20","20","20","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.076500","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Bow/BP_Visual_BowProjectileBase",line): #arrow changes
                removeSpecialEffect = re.sub('/Game/Items/Weapons/Bow/BP_Item_BowProjectileBase.*?"','/Game/Items/Weapons/Bow/BP_Item_BowProjectileBase.BP_Item_BowProjectileBase_C"',line)
                lowerDamage = re.sub('"0\.000000","[2-9]\d","[2-9]\d","0","0","[2-9]\d","[2-9]\d","[2-9]\d","[2-9]\d","0",','"0.000000","0","0","0","0","0","0","0","0","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.153000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)

            if re.search("/Game/Items/Weapons/Throwing/BP_throwing_offhand_axe",line): #throwing axe changes
                removeSpecialEffect = re.sub('/Game/Items/BP_ProjectileWeaponThrown_.*?"','/Game/Items/BP_ProjectileWeaponThrown.BP_ProjectileWeaponThrown_C"',line)
                lowerDamage = re.sub('"250\.000000","[3-9]\d","[3-9]\d","0","0","[3-9]\d","[3-9]\d","[3-9]\d","[3-9]\d","0",','"250.000000","36","36","0","0","36","36","36","36","0",',removeSpecialEffect)
                lowerArpen = re.sub('"(4|5)","0.[0-9]*?","0","0","0","0"','"4","0.000000","0","0","0","0"',lowerDamage)
                tableOutput.write(lowerArpen)