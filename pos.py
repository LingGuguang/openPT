



def pos(context, pos_type='thulac'):
    return pos_types[pos_type](context)

def pos_thulac(context):
    from thulac import thulac as tlac
    lac = tlac(seg_only=False)
    return lac.cut(context, text=True)

def pos_baidulac(context):
    from LAC import LAC
    lac = LAC(mode='lac')
    return lac.run(context)


pos_types = {
    'thulac': pos_thulac,
    'baidulac': pos_baidulac
}


if __name__ == "__main__":
    text = "今天的街道好安静啊"
    print(pos(text, pos_type='baidulac'))